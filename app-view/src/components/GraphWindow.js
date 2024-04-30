import { Graph } from "react-d3-graph";
import { useQueryClient, useQuery } from '@tanstack/react-query';
import { useState } from "react";
import { useRef } from "react";
import { get_graph } from "../adapters/GraphAdapter.js";
import { FINISHED_STATE, NON_SELECTED } from "../globals/globalVars.js";
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
  const graphRef = useRef(null);
  
  const graph_query = useQuery({
    queryKey: ['graph'],
    queryFn: get_graph
  });
  
  const informUserAboutInstruction = (instruction) => {
    if(refToInstructions?.current)
      refToInstructions.current.innerText = instruction;
  }

  const clearInstructions = (timeout) => {
    timeout = typeof timeout !== 'undefined' ? timeout : 0;
    setTimeout(informUserAboutInstruction, timeout, '');
  }

  console.log("parsed graph response - ", JSON.parse(JSON.stringify(graph_query.data ? graph_query.data : {'graph': {}})));
  let temp_data = {'nodes': [], 'links': []};
  if(graph_query.isSuccess)
  {
    temp_data = takeDataFromResponse(graph_query.data);
    if(graph_query.data.algorithm?.currentState === FINISHED_STATE){
      informUserAboutInstruction("Done! Path has been found!");
    }
    console.log('actual parsed graph data - ', temp_data);
  }
  
  const data = temp_data;
  const [actualData, setActualData] = useState({data: data});
  const graphWindowRef = useRef(this);

  const [clearGraphMutation, addNodeMutation, addEdgeMutation, removeNodeMutation, removeEdgeMutation] = useMutationsForGraph({queryClient});

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
          ref={graphRef}
          data={data}
          config={config}
          onClickNode={handleClickNode}
          onClickLink={handleClickLink}
          onDoubleClickNode={handleDoubleClickNode}
          resetNodesPositions={true}
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
        data={actualData}
        setData={setActualData}
        refs={[sourceRef, targetRef, graphRef, graphWindowRef]}
        queryClient={queryClient}
      />
    </>);
};

export default GraphWindow;
