from flask import Flask, jsonify, url_for, request, logging
from flask_cors import CORS
from main import database
from src.graph_response_parser import GraphResponseParser

# instantiate Flask functionality
app = Flask(__name__)
CORS(app)


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
    return jsonify(response)


@app.route("/graph", methods=["GET"])
def get_graph():
    response = GraphResponseParser.get_graph()
    return jsonify(response)


@app.route("/node", methods=["POST"])
def add_node():
    response = GraphResponseParser.add_node()
    return jsonify(response)


@app.route("/node/<node_id>", methods=["DELETE"])
def remove_node(node_id):
    response = GraphResponseParser.remove_node(int(node_id))
    return jsonify(response)


@app.route("/edges/<node_id1>/<node_id2>", methods=["POST"])
def add_edge(node_id1, node_id2):
    response = GraphResponseParser.add_edge(int(node_id1), int(node_id2))
    return jsonify(response)


@app.route("/edges/<node_id1>/<node_id2>", methods=["DELETE"])
def remove_edge(node_id1, node_id2):
    response = GraphResponseParser.remove_edge(int(node_id1), int(node_id2))
    return jsonify(response)


@app.route("/database", methods=["GET"])
def get_database():
    return jsonify(database.get_tables())
