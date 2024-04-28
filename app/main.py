from app.src.model.algorithms.dfs import DFS
from app.src.model.graph.undirectedgraph import UndirectedGraph
from src.persistence.mock_database import MockDatabase
import wsgi
from logging.config import dictConfig


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

HOST_TO_RUN_ON = '0.0.0.0'

graph = UndirectedGraph()
database = MockDatabase()
algorithm = DFS()


def change_algorithm(new_algo):
    global algorithm
    algorithm = new_algo


if __name__ == "__main__":
    wsgi.app.run(host=HOST_TO_RUN_ON, debug=True)
