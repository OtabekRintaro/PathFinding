from flask import Flask, jsonify, url_for, request, logging
from flask_cors import CORS

from app.src.algorithm_response_handler import AlgorithmResponseHandler
from main import Storage
from src.graph_response_handler import GraphResponseHandler

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


@app.route("/graph/<graph_type_name>", methods=["PUT"])
def set_graph_type(graph_type_name):
    response = GraphResponseHandler.set_graph_type(graph_type_name)
    return jsonify(response)


@app.route("/graph/<graph_file_index>", methods=["POST"])
def import_graph_from_file(graph_file_index):
    content = {}
    if request and request.json:
        content = request.json
    print('got to sending response')
    response = GraphResponseHandler.import_ready_graph(int(graph_file_index), content.get('isE2E', '') == 'True')
    return jsonify(response)


@app.route("/graph", methods=["DELETE"])
def clear_graph():
    response = GraphResponseHandler.clear_graph()
    return jsonify(response)


@app.route("/graph", methods=["GET"])
def get_graph():
    response = GraphResponseHandler.get_graph()
    response.update(AlgorithmResponseHandler.get_algorithm())
    return jsonify(response)


@app.route("/node", methods=["POST"])
def add_node():
    response = GraphResponseHandler.add_node()
    return jsonify(response)


@app.route("/node/<node_id>", methods=["DELETE"])
def remove_node(node_id):
    response = GraphResponseHandler.remove_node(int(node_id))
    return jsonify(response)


@app.route("/edges/<node_id1>/<node_id2>", methods=["POST"])
def add_edge(node_id1, node_id2):
    response = GraphResponseHandler.add_edge(int(node_id1), int(node_id2))
    return jsonify(response)


@app.route("/edges/<node_id1>/<node_id2>/<weight>", methods=["POST"])
def add_edge_with_weight(node_id1, node_id2, weight):
    response = GraphResponseHandler.add_edge(int(node_id1), int(node_id2), int(weight))
    return jsonify(response)

@app.route("/edges/<node_id1>/<node_id2>/<weight>", methods=["PUT"])
def set_weight(node_id1, node_id2, weight):
    response = GraphResponseHandler.set_weight(int(node_id1), int(node_id2), int(weight))
    return jsonify(response)


@app.route("/edges/<node_id1>/<node_id2>", methods=["DELETE"])
def remove_edge(node_id1, node_id2):
    response = GraphResponseHandler.remove_edge(int(node_id1), int(node_id2))
    return jsonify(response)


@app.route("/database", methods=["GET"])
def get_database():
    return jsonify(Storage.database.get_tables())


@app.route("/algorithm/<algorithm_name>", methods=["PUT"])
def change_algorithm(algorithm_name):
    AlgorithmResponseHandler.choose_algorithm(algorithm_name)
    return jsonify()


@app.route("/algorithm/<source>/<target>", methods=["POST"])
def run_algorithm(source, target):
    response = AlgorithmResponseHandler.run_algorithm(int(source), int(target))
    return jsonify(response)


@app.route("/algorithm/next_step", methods=["PUT"])
def do_step():
    response = AlgorithmResponseHandler.do_step()
    return jsonify(response)


@app.route("/algorithm", methods=["DELETE"])
def clear_algorithm():
    response = AlgorithmResponseHandler.clear_algorithm()
    return jsonify(response)
