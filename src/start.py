
from flask import Flask, request
from transform import layout
import sys
import json
app = Flask(__name__)

@app.route('/layout', methods=['GET','POST'])
def dataTransform():
    data = json.loads(request.get_data(as_text=True))
    # reMap=data.nodes
    # data = request.get_data(as_text=True)
    layout(data)

    # with open(filename, 'w') as file_obj:
    #     json.dump(data, file_obj)
    # calLayout(filename=filename, originDataJsonObject=data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
