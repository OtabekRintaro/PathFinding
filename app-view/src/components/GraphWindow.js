import { Graph } from "react-d3-graph";
import { useQueryClient, useQuery } from '@tanstack/react-query';
import { useState } from "react";
import { useRef } from "react";
import { get_graph } from "../adapters/GraphAdapter.js";
import { NON_SELECTED } from "../globals/globalVars.js";
import useMutationsForGraph from "../hooks/useMutationsForGraph.js";
import graphDataManipulation from "../utils/graphDataManipulation.js";
import { takeDataFromResponse } from "../utils/takeDataFromResponse.js";
import GraphControlDisplay from "./GraphControlDisplay.js";
import AlgorithmControlDisplay from "./AlgorithmControlDisplay.js";
import algorithmDataManipulation from "../utils/algorithmDataManipulation.js";

const GraphWindow = () => {
  const queryClient = useQueryClient();
  const config = require("../globals/config.js").default;
  const refToInstructions = useRef(null);
  const sourceRef = useRef(null);
  const targetRef = useRef(null);

  const graph_query = useQuery({
    queryKey: ['graph'],
    queryFn: get_graph
  });
  
  console.log("parsed graph response - ", JSON.parse(JSON.stringify(graph_query)));
  let temp_data = {nodes: [], links: []};
  if(graph_query.isSuccess)
  {
    temp_data = takeDataFromResponse(graph_query.data);
    console.log('actual parsed graph data - ', temp_data);
  }

  const data = temp_data;

  const [clearGraphMutation, addNodeMutation, addEdgeMutation, removeNodeMutation, removeEdgeMutation] = useMutationsForGraph({queryClient});

  const informUserAboutInstruction = (instruction) => {
    refToInstructions.current.innerText = instruction;
  }

  const clearInstructions = () => {
    informUserAboutInstruction('');
  }

  const [action, setAction] = useState('')
  const [selectedId, setSelectedId] = useState(NON_SELECTED);
  const [handleClickNode, handleClickLink] = graphDataManipulation({action, setAction, selectedId, setSelectedId, addEdgeMutation, removeNodeMutation, removeEdgeMutation, informUserAboutInstruction, clearInstructions});
  const [handleDoubleClickNode] = algorithmDataManipulation({action, setAction, sourceRef, targetRef, informUserAboutInstruction, clearInstructions});

  console.log('current action', action);

  return (
    <>
      <p ref={refToInstructions}></p>
      <Graph 
          id="graph-id"
          data={data}
          config={config}
          onClickNode={handleClickNode}
          onClickLink={handleClickLink}
          onDoubleClickNode={handleDoubleClickNode}
      />
      <GraphControlDisplay 
        setAction={setAction}
        informUserAboutInstruction={informUserAboutInstruction}
        mutations={[addNodeMutation, clearGraphMutation]}
        clearInstructions={clearInstructions}
      />
      <AlgorithmControlDisplay
        informUserAboutInstruction={informUserAboutInstruction}
        clearInstructions={clearInstructions}
        setAction={setAction}
        refs={[sourceRef, targetRef]}
        queryClient={queryClient}
      />
    </>);
};

export default GraphWindow;
