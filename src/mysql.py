import pymysql
import networkx as nx
import math
import json
from networkx.readwrite import json_graph

global cursor
def saveGraph():
    sql = "SELECT id, company_id, role_id, role_name, role_type, company_role, equity_ratio, dgraph_mark, unix_timestamp(establishment_date), unix_timestamp(role_company_establishment_date) FROM graph_inference.dw_companytime1 where establishment_date is not null and role_company_establishment_date is not null;"
    cursor.execute(sql)
    data = cursor.fetchall()
    G = nx.Graph()
    for item in data:
        _id,_company_id,_role_id, _role_name,_role_type,_company_role, _equity_ratio, _dgraph_mark, time0, time1  = item
        if time0 <=0 or time1<=0:
            continue
        time = time0
        if time < time1:
            time =time1
        source = str(_company_id)
        target = str(_role_id)
        if source == target:
            continue
        G.add_edge(source,target,timestamp = time)
    remove = [node for node,degree in G.degree().items() if degree > 2]
    G.remove_nodes_from(remove)
    connect_graphs = nx.connected_components(G)
    largest_cc = max(connect_graphs, key=len)
    H = G.subgraph(largest_cc)
        # result['nodes'].add(source)
        # result['nodes'].add(target)
        # result['links'].append({'source':source,'target':target})
    f= open('graph.json','w')
    result = json_graph.node_link_data(H)
    json.dump(result,f)
    f.close()

def connect():
    global cursor
    conn  = pymysql.connect(host='10.5.24.98',
                        port =3306,
                        user = 'downsee',
                        passwd = 'Zjlab$downsee123'    )
    cursor = conn.cursor()
    return cursor

def add_attribute():


if __name__ == "__main__":
    connect()
    saveGraph()
    # add_attribute()