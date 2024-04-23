from app.src.model.undirectedgraph import UndirectedGraph
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

graph = UndirectedGraph()
database = MockDatabase()

if __name__ == "__main__":
    wsgi.app.run(debug=True)
