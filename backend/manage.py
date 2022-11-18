import json
import random
import gevent

from gevent import monkey
monkey.patch_all()

from geventwebsocket._compat import range_type

from flask import Flask, app, render_template, request, jsonify
from flask_cors import CORS
from werkzeug.debug import DebuggedApplication

from geventwebsocket import WebSocketServer, WebSocketApplication, Resource

import store

app = Flask(__name__)
app.debug = True
CORS(app)

suppliesDataSets = store.suppliesDataSets

weight = 0

class GraphApplication(WebSocketApplication):
    def on_open(self):
       print("Connection open!")

    def broadcast(self, weight):
        for client in self.ws.handler.server.clients.values():
            client.ws.send(json.dumps({
                'msg_type': 'update_graph',
                'weight': str(weight)
            }))

    def on_close(self, reason):
        print("Connection closed! ")


app = Flask(__name__, static_folder='../frontend/dist/static', template_folder='../frontend/dist')
#app = Flask(__name__, template_folder='./')

@app.route('/receive', methods=["POST"])
def recieve():
    global weight
    if request.method == "POST":
        weight = request.json.get("weight")
        """
        t = int(time.mktime(datetime.datetime.now().timetuple()))
        jsonData = {"time": t, "": weight}
        #print(weight)
        ws.send('graph_update', jsonData)
        print(jsonData)"""

    return {"status": "ok"}

@app.route('/api/getSuppliesDataSets', methods=["GET"])
def getDataSets():
    #global suppliesDataSets
    return jsonify({"dataSet": suppliesDataSets}), 200


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:warehouseId>/food')
@app.route('/<int:warehouseId>/drink')
@app.route('/<int:warehouseId>/medicine')
def indexSub(warehouseId):
    return render_template('index.html')


resource = Resource([
    ('^/graph', GraphApplication),
    ('^/.*', DebuggedApplication(app))
])

if __name__ == "__main__":
    WebSocketServer(
        ('0.0.0.0', 5000),
        resource,
        debug=False
    ).serve_forever()
