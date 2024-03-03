from src.mock_database import MockDatabase
import wsgi
from src.model.graph import UndirectedGraph

graph = UndirectedGraph()
database = MockDatabase()

if __name__ == "__main__":
    wsgi.app.run(debug=True)
