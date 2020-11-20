
from flask import Flask, request
from flask_cors import CORS
from transform import layout
from fun import deal_emb
import json
app = Flask(__name__)
CORS(app)
global results
@app.route('/layout', methods=['GET','POST'])
def dataTransform():
    data = json.loads(request.get_data(as_text=True))
    graph=data['graph']
    params=data['params']
    layout(graph,params)
    return data

@app.route('/get_graph',methods=['GET','POST'])
def get_graph():
    global results
    return results
    
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

def start():
    global results
    f = open('./graph_degree.json','r')
    results = json.load(f)
    f.close()

if __name__ == '__main__':
    start()
    app.run(host='0.0.0.0', port=5000)
