import './App.css';
import {
  Routes, Route, Link
} from 'react-router-dom';
import UndirectedGraphWindow from './components/UndirectedGraphWindow.js';
import DirectedGraphWindow from './components/DirectedGraphWindow.js';
import Index from './components/Index.js';
import { set_graph_type, clear_graph, get_graph } from "./adapters/GraphAdapter.js";
import { useMutation, useQueryClient, useQuery } from '@tanstack/react-query';

function App() {
  const queryClient = useQueryClient();

  const graph_query = useQuery({
    queryKey: ['graph'],
    queryFn: get_graph
  });
  
  const config = require("./globals/config.js").default;

  const clearGraphMutation = useMutation({mutationFn: clear_graph, onSuccess: () => queryClient.invalidateQueries(['graph'])});
  const setGraphMutation = useMutation({mutationFn: set_graph_type});
  
  const padding = {
    padding: 5
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>
          PATH FINDING ALGOS
        </p>
          <div>
            <Link style={padding} to="/" onClick={() => clearGraphMutation.mutate()}>Home</Link>
            <Link style={padding} to="/undirected" onClick={() => {clearGraphMutation.mutate(); setGraphMutation.mutate('undirected');}}>Undirected Graph</Link>
            <Link style={padding} to="/directed" onClick={() => {clearGraphMutation.mutate(); setGraphMutation.mutate('directed');}}>Directed graph</Link>
          </div>
        
          <Routes>
            <Route path="/undirected" element={<UndirectedGraphWindow graph_query={graph_query} config={config}/>} />
            <Route path="/directed" element={<DirectedGraphWindow graph_query={graph_query} config={config}/>} />
            <Route path="/" element={<Index />} />
          </Routes>
      </header>
    </div>
  );
}

export default App;
