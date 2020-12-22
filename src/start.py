
from flask import Flask, request
from flask_cors import CORS
from transform import fm3, circular_OGDF
from fun import deal_emb
import json
import time
import copy
import random

app = Flask(__name__)
CORS(app)
global results
@app.route('/fm3_layout', methods=['GET', 'POST'])
def fm3_layout():
    data = request.json
    graph = data['graph']
    params = {}
    if 'params' in data:
        params = data['params']
    fm3(graph, params)
    return data


@app.route('/circular_OGDF_layout', methods=['GET', 'POST'])
def circular_OGDF_layout():
    data = request.json
    graph = data['graph']
    params = {}
    if 'params' in data:
        params = data['params']
    circular_OGDF(graph, params)
    return data


@app.route('/get_share_holding_graph', methods=['GET', 'POST'])
def get_share_holding_graph():
    global results
    return results['share_holding']


@app.route('/get_health_care_graph', methods=['GET', 'POST'])
def get_health_care_graph():
    global results
    return results['health_care']


@app.route('/get_health_care_graph_small', methods=['GET', 'POST'])
def get_health_care_graph_small():
    global results
    return results['health_care_small']


@app.route('/emb', methods=['GET', 'POST'])
def dataEmb():
    data = request.json
    graph = data['graph']
    results = {}
    emb, anomaly_nodes, projection_nodes, community_nodes = deal_emb(graph)
    results['anomaly'] = anomaly_nodes
    results['projection'] = projection_nodes
    results['community'] = community_nodes
    return json.dumps(results)


def isGraphsLayouted(graphs):
    flag = True
    for timestamp in graphs:
        graph = graphs[timestamp]
        for node in graph['nodes']:
            if 'x' not in node and 'y' not in node:
                flag = False
                break
        if not flag:
            break
    return flag


def start():
    global results
    results = {}
    f = open('./share_holding.json', 'r')
    results['share_holding'] = json.load(f)
    f.close()
    f = open('./share_holding_attributes.json', 'r', encoding='UTF-8')
    attributes = json.load(f)
    for node in results['share_holding']['nodes']:
        attribute = attributes[node['id']]
        for key in attribute:
            node[key] = attribute[key]
    f.close()
    health_care_filename = './health_care_graph_fake.json'
    f = open(health_care_filename, 'r', encoding='UTF-8')
    results['health_care'] = json.load(f)
    f.close()

    if health_care_filename == './health_care_graph_daily_Oct2June.json':  # remove links later than 2020/06/27
        links = []
        for link in results['health_care']['links']:
            if link['timestamp'] <= 1593187200:
                links.append(link)
        for node in results['health_care']['nodes']:
            if 'attr' in node:
                for timestamp in node['attr']:
                    if int(timestamp) >= 1590595200:
                        node['attr'][timestamp]['anomaly1'] = None
                        node['attr'][timestamp]['anomaly2'] = None
        results['health_care']['links'] = links

    if health_care_filename == './health_care_graph_fake.json':
        graphs = results['health_care']
        graph = graphs['2020/5']

        # add links
        node_set = set(("37536924", "37086978", "74535899", "37216687", "38224680", "37131349", '4027'))
        for node in graph['nodes']:
            if node['id'] in node_set:
                for time_key in node['attr']:
                    if 'total_money' in node['attr'][time_key] and node['attr'][time_key]['ratio'] <= 0.7:
                        ratio = round(random.uniform(0.7, 1), 2)
                        total_money = round(random.uniform(30, 200), 2)
                        node['attr'][time_key]['ratio'] = ratio
                        node['attr'][time_key]['total_money'] = total_money
                        node['attr'][time_key]['country_money'] = total_money * ratio  # country_money
                        node['attr'][time_key]['count'] = random.randint(5, 30)
                        node['attr'][time_key]['average_price'] = total_money / node['attr'][time_key]['count']
        new_links = []
        for link in graph['links']:
            if link['source'] in node_set and link['target'] in node_set:
                if link['timestamp'] == 1588694400:
                    new_link = copy.deepcopy(link)
                    new_link['timestamp'] += 24 * 60 * 60
                    new_links.append(new_link)
                    new_link = copy.deepcopy(link)
                    new_link['timestamp'] += 3 * 24 * 60 * 60
                    new_links.append(new_link)
                    new_link = copy.deepcopy(link)
                    new_link['timestamp'] += 10 * 24 * 60 * 60
                    new_links.append(new_link)
                else:
                    new_links = []
                    break

        for link in new_links:
            graph['links'].append(link)

        graphs['2020/5'] = graph

        graph = graphs['2020/6']
        # remove links
        links_tobe_removed = []
        link_map = {}
        node_set = {'267727', '4662527', '2495112'}
        for node in graph['nodes']:
            if node['id'] in node_set:
                for time_key in node['attr']:
                    if 'total_money' in node['attr'][time_key] and node['attr'][time_key]['ratio'] > 0.7:
                        ratio = round(random.uniform(0, 0.7), 2)
                        node['attr'][time_key]['ratio'] = ratio
                        total_money = node['attr'][time_key]['total_money']
                        node['attr'][time_key]['country_money'] = total_money * ratio  # country_money
        for link in graph['links']:
            if link['target'] in node_set or link['source'] in node_set:
                if link['source'] == '9218':
                    if link['target'] in link_map:
                        link_map[link['target']] += 1
                        if link_map[link['target']] > 5:
                            links_tobe_removed.append(link)
                    else:
                        link_map[link['target']] = 1
                if link['target'] == '9218':
                    if link['source'] in link_map:
                        link_map[link['source']] += 1
                        if link_map[link['source']] > 5:
                            links_tobe_removed.append(link)
                    else:
                        link_map[link['source']] = 1

        for link in links_tobe_removed:
            graph['links'].remove(link)

        graphs['2020/6'] = graph

        f = open(health_care_filename, 'w', encoding='UTF-8')
        json.dump(graphs, f)
        f.close()





    # layout
    if not isGraphsLayouted(results['health_care']):
        graphs = results['health_care']
        for timestamp in graphs:
            graph = graphs[timestamp]
            fm3(graph, {})
            graphs[timestamp] = graph
        f = open(health_care_filename, 'w', encoding='UTF-8')
        json.dump(graphs, f)
        f.close()

    health_care_test_filename = './health_care_graph_test.json'
    f = open(health_care_test_filename, 'r', encoding='UTF-8')
    results['health_care_small'] = json.load(f)
    f.close()

    if health_care_test_filename == './health_care_graph_test.json' and 'nodes' in results['health_care_small']:
        result = {}
        graph = results['health_care_small']
        links = graph['links']
        nodes = graph['nodes']
        hospitals = {}
        for node in nodes:
            if 'type' in node:
                hospitals[node['id']] = node
            split_nodes = {}
            if 'attr' in node:
                for timestamp in node['attr']:
                    year = time.localtime(int(timestamp)).tm_year
                    mon = time.localtime(int(timestamp)).tm_mon
                    key = str(year) + '/' + str(mon)
                    if key not in split_nodes:
                        split_nodes[key] = copy.deepcopy(node)
                        split_nodes[key]['attr'] = {
                            timestamp: split_nodes[key]['attr'][timestamp]
                        }
                    else:
                        split_nodes[key]['attr'][timestamp] = copy.deepcopy(
                            node['attr'][timestamp])
            for key in split_nodes:
                if key not in result:
                    result[key] = {
                        'nodes': {},
                        'links': []
                    }
                result[key]['nodes'][split_nodes[key]['id']] = split_nodes[key]
        for link in links:
            timestamp = link['timestamp']

            year = time.localtime(timestamp).tm_year
            mon = time.localtime(timestamp).tm_mon
            key = str(year) + '/' + str(mon)
            if key not in result:
                result[key] = {
                    'nodes': {},
                    'links': []
                }
            result[key]['links'].append(link)

            if link['source'] in hospitals:
                if link['source'] not in result[key]['nodes']:
                    result[key]['nodes'][link['source']
                                         ] = hospitals[link['source']]

            if link['target'] in hospitals:
                if link['target'] not in result[key]['nodes']:
                    result[key]['nodes'][link['target']
                                         ] = hospitals[link['target']]

        for key in result:
            result[key]['nodes'] = list(result[key]['nodes'].values())
        results['health_care_small'] = result

    if not isGraphsLayouted(results['health_care_small']):
        graphs = results['health_care_small']
        for timestamp in graphs:
            graph = graphs[timestamp]
            fm3(graph, {})
            graphs[timestamp] = graph
        f = open(health_care_test_filename, 'w', encoding='UTF-8')
        json.dump(graphs, f)
        f.close()


if __name__ == '__main__':
    start()
    app.run(host='0.0.0.0', port=5000)
