from flask import Flask, jsonify, url_for, request, logging, abort
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

    urls.append("METHOD: PUT, " + url_for('set_graph_type', graph_type_name="graph_type_name"))
    urls.append("METHOD: POST, " + url_for('import_graph_from_file', graph_file_index="graph_file_index"))
    urls.append("METHOD: DELETE, " + url_for('clear_graph'))
    urls.append("METHOD: GET, " + url_for('get_graph'))
    urls.append("METHOD: POST, " + url_for('add_node'))
    urls.append("METHOD: DELETE, " + url_for('remove_node', node_id="node_id"))
    urls.append("METHOD: POST, " + url_for('add_edge', node_id1="first_node_id", node_id2="second_node_id"))
    urls.append("METHOD: POST, " + url_for('add_edge_with_weight', node_id1="first_node_id",
                                           node_id2="second_node_id", weight="weight"))
    urls.append("METHOD: PUT, " + url_for('set_weight', node_id1="first_node_id",
                                           node_id2="second_node_id", weight="weight"))
    urls.append("METHOD: GET, " + url_for('get_database'))
    urls.append("METHOD: PUT, " + url_for('change_algorithm', algorithm_name="algorithm_name"))
    urls.append("METHOD: POST, " + url_for('run_algorithm', source="source_node_id",
                                           target="target_node_id"))
    urls.append("METHOD: PUT, " + url_for('do_step'))
    urls.append("METHOD: DELETE, " + url_for('clear_algorithm'))
    urls.append("METHOD: DELETE, " + url_for('remove_edge', node_id1="first_node_id", node_id2="second_node_id"))

    for i in range(1, len(urls)):
        urls[i] = f'{urls[i]} <br/><br/>'

    return "".join(urls)


@app.errorhandler(500)
def internal_server_error(e):
    print('Error: ', str(e))
    return jsonify(error=str(e)), 500


@app.route("/graph/<graph_type_name>", methods=["PUT"])
def set_graph_type(graph_type_name):
    response = GraphResponseHandler.set_graph_type(graph_type_name)
    return jsonify(response)


@app.route("/graph/<graph_file_index>", methods=["POST"])
def import_graph_from_file(graph_file_index):
    print('got to sending response')
    try:
        response = GraphResponseHandler.import_ready_graph(int(graph_file_index))
    except Exception as e:
        print('Error: ', str(e))
        abort(500, description=e)

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
    response = GraphResponseHandler.add_edge(int(node_id1), int(node_id2), float(weight))
    return jsonify(response)


@app.route("/edges/<node_id1>/<node_id2>/<weight>", methods=["PUT"])
def set_weight(node_id1, node_id2, weight):
    response = GraphResponseHandler.set_weight(int(node_id1), int(node_id2), float(weight))
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
