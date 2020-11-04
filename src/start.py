
from flask import Flask, request
from transform import layout
import json
app = Flask(__name__)

@app.route('/layout', methods=['GET','POST'])
def dataTransform():
    data = json.loads(request.get_data(as_text=True))
    graph=data['graph']
    params=data['params']
    layout(graph,params)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
