import json

import networkx as nx
import pymysql
from networkx.readwrite import json_graph

global cursor


def saveGraph():
    sql = "SELECT id, company_id, role_id, role_name, role_type, company_role, equity_ratio, dgraph_mark, unix_timestamp(establishment_date), unix_timestamp(role_company_establishment_date),equity_ratio FROM graph_inference.dw_companytime1 where establishment_date is not null and role_company_establishment_date is not null;"
    cursor.execute(sql)
    data = cursor.fetchall()
    G = nx.Graph()
    for item in data:
        _id, _company_id, _role_id, _role_name, _role_type, _company_role, _equity_ratio, _dgraph_mark, time0, time1,equity_ratio = item
        if time0 <= 0 or time1 <= 0:
            continue
        time = time0
        if time < time1:
            time = time1
        source = str(_company_id)
        target = str(_role_id)
        if source == target:
            continue
        G.add_edge(source, target, timestamp=time)
        if equity_ratio!= None:
            G.nodes[source]['equity_ratio'] = float(equity_ratio)
        else:
            G.nodes[source]['equity_ratio'] = None
    for i in range(5):
        remove = [node for node, degree in G.degree() if degree <= 1]
        G.remove_nodes_from(remove)
        print(len(G.nodes), len(G.edges()))
    connect_graphs = nx.connected_components(G)
    largest_cc = max(connect_graphs, key=len)
    H = G.subgraph(largest_cc)
    # result['nodes'].add(source)
    # result['nodes'].add(target)
    # result['links'].append({'source':source,'target':target})
    f = open('graph_degree.json', 'w')
    result = json_graph.node_link_data(H)
    json.dump(result, f)
    f.close()


def connect():
    global cursor
    conn = pymysql.connect(host='10.5.24.98',
                           port=3306,
                           user='downsee',
                           passwd='Zjlab$downsee123')
    cursor = conn.cursor()
    return cursor


def add_attribute():
    f = open('graph_degree.json', 'r')
    graph = json.load(f)
    f.close()
    result = {}
    i = 0
    for node in graph['nodes']:
        id = node['id']
        if 'equity_ratio' in node:
            equity_ratio = node['equity_ratio']
        else:
            equity_ratio = None
        sql = "Select reg_capital,reg_capital, chi_name,company_type, business_scope,reg_addr from graph_inference.dw_company where graph_inference.dw_company.id =" + str(
            id) + ';'
        cursor.execute(sql)
        data = cursor.fetchone()
        reg_capital, reg_capital, chi_name, company_type, business_scope, reg_addr = data
        result[id] = {"reg_capital": reg_capital, "reg_capital": reg_capital, 'chi_name': chi_name,
                      'company_type': company_type, "business_scope": business_scope, "reg_addr": reg_addr,"equity_ratio":equity_ratio}
        i += 1
        if i % 10000 == 0:
            print(i)
    f = open('graph_attr.json', 'w', encoding='utf-8')
    json.dump(result, f, ensure_ascii=False)
    f.close()

def anomaly():
    f = open('graph_attr.json', 'r',encoding='utf-8')
    graph = json.load(f)
    f.close()
    result = {}
    i = 0
    k=0
    for id in graph.keys():
        i += 1
        if i % 1000 == 0:
            print(i)
        node = graph[id]
        sql ="select unix_timestamp(record_time), record_reason from downsee.dw_company_manage_abnormal where company_id =" +str(id)+';'
        cursor.execute(sql)
        data = cursor.fetchall()
        node['anomaly'] = {'manage_abnormal': []}
        if data!= None:
            for item in data:
                record_time, record_reason = item
                if record_time<0:
                    continue
                node['anomaly']['manage_abnormal'].append({'record_time':record_time,'record_reason':record_reason})
        result[id] = node
    print(k)
    f = open('graph_attr_manage_abnormal.json', 'w', encoding='utf-8')
    json.dump(result, f, ensure_ascii=False)
    f.close()

def credit():
    f = open('graph_attr_manage_abnormal.json', 'r',encoding='utf-8')
    graph = json.load(f)
    f.close()
    result = {}
    i = 0
    k=0
    for id in graph.keys():
        i += 1
        if i % 1000 == 0:
            print(i)
        node = graph[id]
        sql ="select unix_timestamp(dishonesty_time), dishonesty_reason from downsee.dw_company_credit where company_id =" +str(id)+';'
        cursor.execute(sql)
        data = cursor.fetchall()
        node['anomaly']['credit'] = []
        if data!= None:
            for item in data:
                dishonesty_time, dishonesty_reason = item
                if dishonesty_time<0:
                    continue
                k+=1
                node['anomaly']['credit'].append({'dishonesty_time':dishonesty_time,'dishonesty_reason':dishonesty_reason})
        result[id] = node
    print(k)
    f = open('graph_attr_manage_credit.json', 'w', encoding='utf-8')
    json.dump(result, f, ensure_ascii=False)
    f.close()

if __name__ == "__main__":
    connect()
    # saveGraph()
    # add_attribute()
    # anomaly()
    credit()