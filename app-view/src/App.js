import {
  Routes, Route, Link
} from 'react-router-dom';
import UndirectedGraphWindow from './components/UndirectedGraphWindow.js';
import DirectedGraphWindow from './components/DirectedGraphWindow.js';
import Index from './components/Index.js';
import { clear_graph, get_graph } from "./adapters/GraphAdapter.js";
import { useMutation, useQueryClient, useQuery } from '@tanstack/react-query';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

function App() {
  const queryClient = useQueryClient();

  const graph_query = useQuery({
    queryKey: ['graph'],
    queryFn: get_graph
  });
  
  const config = require("./globals/config.js").default;

  const clearGraphMutation = useMutation({mutationFn: clear_graph, onSuccess: () => queryClient.invalidateQueries(['graph'])});
  
  const padding = {
    padding: 5
  };

  console.log("rendered");
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark" expand="lg" className="bg-body-tertiary p-3">
        <Container>
          <Navbar.Brand className='text-white'>
                PATH FINDING ALGOS
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav"/>
          <Navbar.Collapse id="basic-navbar-nav" className="justify-content-end">
            <Nav>
              <Nav.Link>
                <Link className='text-white' style={padding} to="/" onClick={() => clearGraphMutation.mutate()}>Home</Link>
              </Nav.Link>
              <Nav.Link>
                <Link className='text-white' style={padding} to="/undirected" onClick={() => clearGraphMutation.mutate()}>Undirected Graph</Link>
              </Nav.Link>
              <Nav.Link>
                <Link className='text-white' style={padding} to="/directed" onClick={() => clearGraphMutation.mutate()}>Directed graph</Link>
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      <Routes>
        <Route path="/undirected" element={<UndirectedGraphWindow graph_query={graph_query} config={config} />} />
        <Route path="/directed" element={<DirectedGraphWindow graph_query={graph_query} config={config}/>} />
        <Route path="/" element={<Index />} />
      </Routes>
    </>
  );
}

export default App;
