import { Graph } from "react-d3-graph";
import { useQueryClient, useMutation, useQuery } from '@tanstack/react-query';
import { get_graph, add_node, add_edge, clear_graph } from "../adapters/GraphAdapter.js";
import { useState } from "react";
import { useRef } from "react";
import { NON_SELECTED } from "../globals/global_vars.js";


const GraphWindow = () => {
  const queryClient = useQueryClient();
  const refToInstructions = useRef(null);
  const config = require("../globals/config.js").default;

  const graph_query = useQuery({
    queryKey: ['graph'],
    queryFn: get_graph
  });
  
  console.log(JSON.parse(JSON.stringify(graph_query)));
  let temp_data = {nodes: [], links: []};
  if(graph_query.isSuccess)
  {
    const take_data = (data_object) => {
      let data_for_graph = {'nodes': [], 'links': []};
      let nodes_for_graph = [];
      let links_for_graph = [];
      const nodes = data_object['graph']['nodes'];
      const links = data_object['graph']['edges'];
      
      if(nodes)
      {
        console.log("retrieved nodes ", data_object['graph']['nodes']);
        const limitHeight = config['height'] - 100;
        const limitWidth = config['width'] - 100;
        let initialX = 50;
        let initialY = 50;
        nodes.forEach(node => {
          nodes_for_graph.push({'id': node.toString(), 'x': initialX, 'y': initialY});
          if(initialX + 15 >= limitWidth)
            initialY = ((initialY + 10) % limitHeight) + 50;
          initialX = ((initialX + 10) % limitWidth) + 50;
        });
        console.log(nodes_for_graph);
        data_for_graph['nodes'] = nodes_for_graph;
      }
      if(links)
      {
        console.log("retrieved edges ",data_object['graph']['edges']);
        Object.entries(links).forEach(edge => {
          const [outNode, inNodes] = edge;
          inNodes.forEach(inNode => links_for_graph.push({"source": outNode, "target": inNode.toString()}));
        })
        data_for_graph['links'] = links_for_graph;
      }
      return data_for_graph;
    };
  
    temp_data = take_data(graph_query.data);
    console.log(temp_data);
  }

  const data = temp_data;

  const clearGraphMutation = useMutation({
    mutationFn: clear_graph,
    onSuccess: () => {
      queryClient.invalidateQueries(['graph']);
    },
  });
  
  const addNodeMutation = useMutation({
    mutationFn: add_node,
    onSuccess: () => {
      queryClient.invalidateQueries(['graph']);
    },
  });

  const addEdgeMutation = useMutation({
    mutationFn: add_edge,
    onSuccess: () => {
      queryClient.invalidateQueries(['graph']);
    },
  });

  const addNode = async (event) => {
    setAction('ADD_NODE');
    addNodeMutation.mutate();
  }
  
  const informUserAboutInstruction = (instruction) => {
    refToInstructions.current.innerText = instruction;
  }
  const clearInstructions = () => {
    informUserAboutInstruction('');
  }

  const [action, setAction] = useState('')
  const startAddEdge = (event) => {
    informUserAboutInstruction('To add and edge - press the nodes you want to link!');
    setAction('ADD_EDGE');
  };

  const [selectedId, setSelectedId] = useState(NON_SELECTED);
  const addEdge = async (node_id1, node_id2) => {
    addEdgeMutation.mutate(selectedId, node_id2);
  }

  const handleClickNode = (nodeId, node) => {
    console.log(`Clicked node ${nodeId} in position (${node.x}, ${node.y})`);
    if(action == 'ADD_EDGE')
    {
      if(selectedId == NON_SELECTED)
      {
        informUserAboutInstruction(`You have selected node ${nodeId}, choose the second node to link!`);
        setSelectedId(nodeId);
      }
      else 
      {
        informUserAboutInstruction(`You have connected nodes ${selectedId} and ${nodeId}!`);
        setTimeout(clearInstructions,5000);
        const newNodeId = nodeId;
        addEdgeMutation.mutate([selectedId, nodeId]);
        setAction('');
        setSelectedId(NON_SELECTED);
      }
    }
  }

  const clearGraph = async () => {
    clearGraphMutation.mutate();
  };

    return (
      <>
        <p ref={refToInstructions}></p>
        <Graph 
            id="graph-id"
            data={data}
            config={config}
            onClickNode={handleClickNode}
        />
        <button onClick={clearGraph}>Clear Graph</button>
        <button onClick={addNode}>Add Node</button>
        <button onClick={startAddEdge}>Add Edge</button>
        {/* <GraphControl/> */}
      </>);
};

export default GraphWindow;