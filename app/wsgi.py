from flask import Flask, json, url_for

from main import database
from src.graph_response_parser import GraphResponseParser

# instantiate Flask functionality
app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Path Finding algos!</p>" + list_of_endpoints()


def list_of_endpoints():
    urls = list()
    urls.append("<h4>API endpoints.</h4>")

    urls.append("METHOD: DELETE, " + url_for('clear_graph'))
    urls.append("METHOD: GET, " + url_for('get_nodes'))
    urls.append("METHOD: POST, " + url_for('add_node'))
    urls.append("METHOD: DELETE, " + url_for('remove_node', node_id="node_id"))
    urls.append("METHOD: POST, " + url_for('add_edge', node_id1="first_node_id", node_id2="second_node_id"))
    urls.append("METHOD: DELETE, " + url_for('remove_edge', node_id1="first_node_id", node_id2="second_node_id"))

    for i in range(1, len(urls)):
        urls[i] = f'{urls[i]} <br/><br/>'

    return "".join(urls)


@app.route("/graph", methods=["DELETE"])
def clear_graph():
    response = GraphResponseParser.clear_graph()
    return json.dumps(response)


@app.route("/nodes", methods=["GET"])
def get_nodes():
    response = GraphResponseParser.get_nodes()
    return json.dumps(response)


@app.route("/node", methods=["POST"])
def add_node():
    response = GraphResponseParser.add_node()
    return json.dumps(response)


@app.route("/node/<node_id>", methods=["DELETE"])
def remove_node(node_id):
    response = GraphResponseParser.remove_node(int(node_id))
    return json.dumps(response)


@app.route("/edges/<node_id1>/<node_id2>", methods=["POST"])
def add_edge(node_id1, node_id2):
    response = GraphResponseParser.add_edge(int(node_id1), int(node_id2))
    return json.dumps(response)


@app.route("/edges/<node_id1>/<node_id2>", methods=["DELETE"])
def remove_edge(node_id1, node_id2):
    response = GraphResponseParser.remove_edge(int(node_id1), int(node_id2))
    return json.dumps(response)


@app.route("/database", methods=["GET"])
def get_database():
    return json.dumps(database.get_tables())
