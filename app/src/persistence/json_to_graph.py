import json
import os.path

from app.src.model.graph.directedgraph import DirectedGraph
from app.src.model.graph.undirectedgraph import UndirectedGraph


class JsonToGraph:

    @staticmethod
    def json_to_graph(json_path, class_of_graph):
        print('opening the json file from - ' + os.getcwd() + os.sep + json_path)
        # if os.environ.get('IsLocalTestRun', '') == 'True':
        #     json_path = '..' + os.sep + '..' + os.sep + '..' + os.sep + '..' + os.sep + json_path
        with open(json_path, 'r') as json_file:
            json_dict = json.load(json_file)
        if class_of_graph is UndirectedGraph:
            new_graph = UndirectedGraph()
        else:
            new_graph = DirectedGraph()

        json_dict = json_dict['graph']
        for _ in json_dict['nodes']:
            new_graph.add_node()

        index = 0
        for edges_of_node in json_dict['edges']:
            for edge in edges_of_node:
                new_graph.add_edge(new_graph.nodes[index], new_graph.nodes[edge[0]], edge[1])
            index += 1

        return new_graph
