from app.src.base_database import BaseDatabase
from app.src.mock_database import MockDatabase
from app import wsgi
from app.src.model.graph import UndirectedGraph, Graph

graph = UndirectedGraph()
database = MockDatabase()

if __name__ == "__main__":
    wsgi.app.run(debug=True)
