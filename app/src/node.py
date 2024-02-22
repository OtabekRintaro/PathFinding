from app.src.id_generator import BaseIDGenerator

KEY_NOT_FOUND = -1

class NodeIDGenerator(BaseIDGenerator):
    ids = list()
    nodes_and_ids = dict()
    node_count = 0

    @staticmethod
    def generate_id_node_pair(node):
        new_id = NodeIDGenerator.generate_id()
        NodeIDGenerator.nodes_and_ids[new_id] = node.__hash__()
        NodeIDGenerator.node_count += 1

    @staticmethod
    def remove_id_of_node(node):
        id = NodeIDGenerator.get_id_of_node(node)
        NodeIDGenerator.remove_id(id)
        for key in range(id, NodeIDGenerator.node_count-1):
            NodeIDGenerator.nodes_and_ids[key] = NodeIDGenerator.nodes_and_ids[key + 1]
        NodeIDGenerator.nodes_and_ids.pop(NodeIDGenerator.node_count-1)
        NodeIDGenerator.node_count -= 1

    @staticmethod
    def get_id_of_node(node):
        node_hash = node.__hash__()
        for key, value in NodeIDGenerator.nodes_and_ids.items():
            if value == node_hash:
                return key
        return KEY_NOT_FOUND

    @staticmethod
    def generate_id():
        new_id = len(NodeIDGenerator.ids)
        NodeIDGenerator.ids.append(new_id)
        return new_id
    
    @staticmethod
    def remove_id(id):
        NodeIDGenerator.ids.pop(id)
        for i in range(id, len(NodeIDGenerator.ids)):
            NodeIDGenerator.ids[i] -= 1
        

class Node():
    def __init__(self):
        NodeIDGenerator.generate_id_node_pair(self)
    
    def __del__(self):
        NodeIDGenerator.remove_id_of_node(self)