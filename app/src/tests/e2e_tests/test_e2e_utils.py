import requests

from app.src.model.node import NodeIDGenerator


def get_ids_and_nodes():
    return NodeIDGenerator.ids_and_nodes


def set_default_undirected_graph():
    requests.post("http://127.0.0.1:5000/node")
    requests.post(f'http://127.0.0.1:5000/node/0')
