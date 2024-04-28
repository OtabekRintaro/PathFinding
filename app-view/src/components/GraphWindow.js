import { Graph } from "react-d3-graph";
import { useQueryClient, useQuery } from '@tanstack/react-query';
import { useState } from "react";
import { useRef } from "react";
import { get_graph } from "../adapters/GraphAdapter.js";
import { NON_SELECTED } from "../globals/globalVars.js";
import useMutationsForGraph from "../hooks/useMutationsForGraph.js";
import graphDataManipulation from "../utils/graphDataManipulation.js";
import { takeDataFromResponse } from "../utils/takeDataFromResponse.js";
import ControlDisplay from "./ControlDisplay.js";


const GraphWindow = () => {
  const queryClient = useQueryClient();
  const refToInstructions = useRef(null);
  const config = require("../globals/config.js").default;

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

  const [action, setAction] = useState('')
  const [selectedId, setSelectedId] = useState(NON_SELECTED);
  const [handleClickNode, handleClickLink] = graphDataManipulation({action, setAction, selectedId, setSelectedId, addEdgeMutation, removeNodeMutation, removeEdgeMutation, informUserAboutInstruction});

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
      />
      <ControlDisplay 
        setAction={setAction}
        informUserAboutInstruction={informUserAboutInstruction}
        mutations={[addNodeMutation, clearGraphMutation]}
      />
    </>);
};

export default GraphWindow;
