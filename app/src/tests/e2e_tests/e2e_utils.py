from app.src.model.graph.node import NodeIDGenerator

RUNNING_STATE = 'running'
FINISHED_STATE = 'finished'


def get_ids_and_nodes():
    return NodeIDGenerator.ids_and_nodes
