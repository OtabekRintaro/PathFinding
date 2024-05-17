import { Graph } from "react-d3-graph";
import { useQueryClient } from '@tanstack/react-query';
import { useState } from "react";
import { useRef } from "react";
import { FINISHED_STATE, NON_SELECTED } from "../globals/globalVars.js";
import { takeDataFromResponse } from "../utils/takeDataFromResponse.js";
import useMutationsForGraph from "../hooks/useMutationsForGraph.js";
import graphDataManipulation from "../utils/graphDataManipulation.js";
import GraphControlDisplay from "./GraphControlDisplay.js";
import AlgorithmControlDisplay from "./AlgorithmControlDisplay.js";
import algorithmDataManipulation from "../utils/algorithmDataManipulation.js";
import DescriptionDisplay from "./DescriptionDisplay.js";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';

const GraphWindow = ({ graph_query, config }) => {
  const queryClient = useQueryClient();
  const refToInstructions = useRef(null);
  const sourceRef = useRef(null);
  const targetRef = useRef(null);
  const weightRef = useRef(null);
  const graphRef = useRef(null);
  
  const informUserAboutInstruction = (instruction) => {
    if(refToInstructions?.current)
      refToInstructions.current.innerText = instruction;
  }

  const clearInstructions = (timeout) => {
    timeout = typeof timeout !== "undefined" ? timeout : 0;
    setTimeout(informUserAboutInstruction, timeout, ['']);
  }

  console.log("parsed graph response - ", JSON.parse(JSON.stringify(graph_query.data ? graph_query.data : {'graph': {}})));
  console.log('path length - ', graph_query?.data?.algorithm?.path?.length);
  let temp_data = {'nodes': [], 'links': []};
  let algorithm_description = "";
  if(graph_query.isSuccess)
  {
    [temp_data, algorithm_description] = takeDataFromResponse(graph_query.data);
    if(graph_query.data.algorithm?.currentState === FINISHED_STATE && graph_query.data.algorithm?.path.length > 0){
      let path_cost = 0;
      if(graph_query.data.algorithm?.pathCost){
        console.log('path cost - ',graph_query.data.algorithm.pathCost);
        path_cost = graph_query.data.algorithm.pathCost;
      }
      informUserAboutInstruction("Done! Path has been found! The path cost is " + path_cost.toString() + "!");
    }else if(graph_query.data.algorithm?.currentState === FINISHED_STATE && graph_query.data.algorithm?.path.length === 0){
      informUserAboutInstruction("There is no path from the source node to the target node!");
    }
    console.log('actual parsed graph data - ', temp_data);

  }
  
  const data = temp_data;

  const [clearGraphMutation, addNodeMutation, addEdgeMutation, setWeightMutation, removeNodeMutation, removeEdgeMutation, setGraphMutation] = useMutationsForGraph({queryClient});

  const [action, setAction] = useState('')
  const [selectedId, setSelectedId] = useState(NON_SELECTED);
  const [handleClickNode, handleClickLink] = graphDataManipulation({action, setAction, selectedId, setSelectedId, weightRef, addEdgeMutation, setWeightMutation, removeNodeMutation, removeEdgeMutation, informUserAboutInstruction, clearInstructions});
  const [handleDoubleClickNode] = algorithmDataManipulation({action, setAction, sourceRef, targetRef, informUserAboutInstruction, clearInstructions});

  console.log('current action', action);

  if(config['directed'] && setGraphMutation.isIdle){
    setGraphMutation.mutate('directed');
  }else if(setGraphMutation.isIdle){
    setGraphMutation.mutate('undirected');
  }

  return (
    <Container>

      <Row className="w-100">
        <Col>
          <p ref={refToInstructions}></p>
        </Col>
        <Col>
          <div style={{ outline: '3px solid red', margin: 0, padding: 0 }}>
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
          </div>
        </Col>
        <Col>
          <DescriptionDisplay 
            description={algorithm_description}
          />
        </Col>
      </Row>
      <Row>
        <Col>
          <GraphControlDisplay 
            setAction={setAction}
            informUserAboutInstruction={informUserAboutInstruction}
            mutations={[addNodeMutation, clearGraphMutation]}
            clearInstructions={clearInstructions}
            weightRef={weightRef}
            queryClient={queryClient}
          />
        </Col>
        <Col>
          <AlgorithmControlDisplay
            informUserAboutInstruction={informUserAboutInstruction}
            clearInstructions={clearInstructions}
            setAction={setAction}
            refs={[sourceRef, targetRef]}
            queryClient={queryClient}
          />
        </Col>
      </Row>
    </Container>);
};

export default GraphWindow;
