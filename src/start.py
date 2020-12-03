
from flask import Flask, request
from flask_cors import CORS
from transform import fm3, circular_OGDF
from fun import deal_emb
import json
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
    f = open('./health_care_graph_hos_March.json', 'r', encoding='UTF-8')
    results['health_care'] = json.load(f)
    f.close()
    f = open('./health_care_graph_test.json', 'r', encoding='UTF-8')
    results['health_care_small'] = json.load(f)
    f.close()


if __name__ == '__main__':
    start()
    app.run(host='0.0.0.0', port=5000)
