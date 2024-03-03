from flask import Flask, json

from main import database
from src.graph_response_parser import GraphResponseParser

# instantiate Flask functionality
app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Path Finding algos!</p>"


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
