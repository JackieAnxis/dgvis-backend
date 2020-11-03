from tulip import tlp
# layout布局算法
# 1. 将图输入方式统一
# 调用tulip实现FM^3布局
def layout(jsonObj):
    nodeMap={}
    graph=tlp.newGraph()
    for node in jsonObj['nodes']:
        n=graph.addNode({"_label":node['id']})
        nodeMap[node['id']]=n
    for link in jsonObj['links']:
        e=graph.addEdge(nodeMap[link['source']],nodeMap[link['target']])  
    params = tlp.getDefaultPluginParameters('FM^3 (OGDF)', graph)
    print('getDefaultPluginParameters finished')
    resultLayout = graph.getLayoutProperty('resultLayout')
    success = graph.applyLayoutAlgorithm('FM^3 (OGDF)', resultLayout, params)
    for node in jsonObj['nodes']:
        node['x']=resultLayout.getNodeValue(nodeMap[node['id']])[0]
        node['y']=resultLayout.getNodeValue(nodeMap[node['id']])[1]
    print('layout finished')
    return jsonObj

if __name__ == '__main__':
    payload = {
            "nodes": [
                {
                    "id": "1583"
                },
                {
                    "id": "1599"
                },
                {
                    "id": "1529"
                },
                {
                    "id": "1510"
                },
                {
                    "id": "1544"
                },
                {
                    "id": "1573"
                },
                {
                    "id": "1549"
                },
                {
                    "id": "1525"
                },
                {
                    "id": "1523"
                },
                {
                    "id": "1602"
                },
                {
                    "id": "1631"
                }
            ],
            "links": [
                {
                    "source": "1583",
                    "target": "1599"
                },
                {
                    "source": "1583",
                    "target": "1510"
                },
                {
                    "source": "1599",
                    "target": "1529"
                },
                {
                    "source": "1599",
                    "target": "1510"
                },
                {
                    "source": "1599",
                    "target": "1523"
                },
                {
                    "source": "1544",
                    "target": "1573"
                },
                {
                    "source": "1549",
                    "target": "1525"
                },
                {
                    "source": "1602",
                    "target": "1631"
                }
            ]
        }
    print(graphTransform(payload))