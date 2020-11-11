
from flask import Flask, request
from transform import layout
from fun import deal_emb
import json
app = Flask(__name__)

@app.route('/layout', methods=['GET','POST'])
def dataTransform():
    data = json.loads(request.get_data(as_text=True))
    graph=data['graph']
    params=data['params']
    layout(graph,params)
    return data

@app.route('/emb',methods=['GET','POST'])
def dataEmb():
    data = request.json
    graph=data['graph']
    results={}
    emb,anomaly_nodes,projection_nodes,community_nodes = deal_emb(graph)
    results['anomaly'] = anomaly_nodes
    results['projection'] = projection_nodes
    results['community'] = community_nodes
    return  json.dumps(results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
