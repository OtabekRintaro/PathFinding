import { useEffect, useRef, useState } from "react";
import Drawing from "./utils/Drawing.js";
import useMousePosition from "./utils/MouseUtils.js";
import { placeIsFree, canConnect, isNode, newArrayWithoutIndex } from "./utils/Checking.js";
import GraphAdapter from "./adapters/GraphAdapter.js";

const Display = () => {
    const actions = {DRAWING : 1, MOVING : 2, ERASING : 3};
    const graphAdapter = new GraphAdapter();
    const widthA = 1000;
    const canvasRef = useRef(null);
    const NON_SELECTED = -1;
    const nodeRadiusBoundary = 25;
    const [typeOfAction, setTypeOfAction] = useState(actions.DRAWING); 
    const [radius, setRadius] = useState([]);
    const [coords, handleCoords] = useMousePosition();
    const [nodes, setNodes] = useState([])
    const [edges, setEdges] = useState([])
    const [typeOfDrawing, setTypeOfDrawing] = useState(0)
    const [selected, setSelected] = useState(NON_SELECTED)

    useEffect(() => {
        if (canvasRef?.current) {
            const ctx = canvasRef.current.getContext("2d");
            const drawing = new Drawing(ctx, 1000, 500);

            drawing.clearCanvas();
            edges.map( (edge, index) => 
                requestAnimationFrame(() => {
                    console.log(edge, index)
                    const startX = nodes[edge.from].x;
                    const startY = nodes[edge.from].y;
                    const endX = nodes[edge.to].x;
                    const endY = nodes[edge.to].y;

                    if(typeOfAction === actions.ERASING && (selected === edge.from || selected === edge.to))
                    drawing.drawEdge(1.7, "red", startX, startY, endX, endY);
                    else
                        drawing.drawEdge(1.7, "white", startX, startY, endX, endY);
                })
            );

            nodes.map((node, index) => 
                requestAnimationFrame(() => {
                    if(index === selected)
                        drawing.drawCircle(radius[index], 1.7, "white", "blue", node.y, node.x);
                    else
                        drawing.drawCircle(radius[index], 1.7, "white", "black", node.y, node.x);
                    if (radius[index] < nodeRadiusBoundary) {
                        let newRadius = radius;
                        newRadius[index] += 0.5;
                        setRadius([ ...newRadius]);
                    }
                })  
            );

        }
    }, [radius, selected, edges, nodes, coords.x, coords.y]);

    return (
        <>
            <canvas
                ref={canvasRef}
                width={widthA.toString()}
                height="550"
                style={{ border: "2px solid black" }}
                onClick={(e) => {
                    const [newX, newY] = handleCoords(e);
                    switch(typeOfAction)
                    {
                        case actions.DRAWING:
                            if(typeOfDrawing === 0 && placeIsFree(nodes, newX, newY, nodeRadiusBoundary)){
                                setNodes(nodes.concat([{ x: newX, y: newY }]));
                                setRadius(radius.concat([15])); 
                                graphAdapter.add_node();

                            }else if(typeOfDrawing === 1)
                            {
                                const newPoint = { x: newX, y: newY }
                                const current_node_index = isNode(nodes, newPoint, nodeRadiusBoundary);
        
                                console.log("current node index", current_node_index);
        
                                if(selected === NON_SELECTED)
                                {
                                    if(current_node_index !== undefined){
                                        console.log("new first node", current_node_index);
                                        setSelected(current_node_index);
                                    }
                                }else{
                                    if(current_node_index !== undefined && canConnect(edges, selected, current_node_index))
                                        setEdges(edges.concat([{ from: selected, to: current_node_index }]));
                                    setSelected(NON_SELECTED);
                                }
                                
                            }
                            break;
                        case actions.MOVING:
                            if(typeOfDrawing === 0)
                            {
                                const newPoint = { x: newX, y: newY }
                                
                                if(selected === NON_SELECTED)
                                {
                                    const current_node_index = isNode(nodes, newPoint, nodeRadiusBoundary);
                                    if(current_node_index !== undefined)
                                    {
                                        console.log("chosen node to move", current_node_index);
                                        setSelected(current_node_index);
                                    }
                                }else{
                                    const current_node_index = isNode(nodes, newPoint, nodeRadiusBoundary * 2);
                                    if(current_node_index === undefined)
                                    {
                                       const newNodes = nodes;
                                       newNodes[selected] = {x: newX, y:newY};
                                       setNodes([...newNodes]);
                                       setSelected(NON_SELECTED); 
                                    }
                                }
                            }
                            break;
                        case actions.ERASING:
                            if(typeOfDrawing === 0)
                            {
                                const newPoint = { x: newX, y: newY }
                                
                                const current_node_index = isNode(nodes, newPoint, nodeRadiusBoundary);
                                if(current_node_index !== undefined)
                                {
                                    setNodes(newArrayWithoutIndex(nodes, current_node_index));
                                    setEdges(() => edges.filter((edge) => edge.from !== current_node_index && edge.to !== current_node_index));
                                }
                            }else if(typeOfDrawing === 1)
                            {
                                const newPoint = { x: newX, y: newY }
                                const current_node_index = isNode(nodes, newPoint, nodeRadiusBoundary);
        
                                console.log("current node index", current_node_index);
        
                                if(selected === NON_SELECTED)
                                {
                                    if(current_node_index !== undefined){
                                        console.log("first node of the edge for removal", current_node_index);
                                        setSelected(current_node_index);
                                    }
                                }else{
                                    if(current_node_index !== undefined && !canConnect(edges, selected, current_node_index))
                                        setEdges(newArrayWithoutIndex(edges, edges.findIndex((edge) => (edge.from === selected && edge.to === current_node_index) 
                                                                                                        ||
                                                                                                        (edge.to === selected && edge.from === current_node_index))));
                                    setSelected(NON_SELECTED);
                                }
                            }
                            break;
                        default:
                            console.log("Error: Type of action #", typeOfAction, " is unknown!");
                            break;
                    }
                }}
            />
            <button onClick={() => { setTypeOfAction(actions.DRAWING); setTypeOfDrawing(0); }} >Nodes</button>
            <button onClick={() => { setTypeOfAction(actions.DRAWING); setTypeOfDrawing(1); }} >Edges</button>
            <button onClick={() => { setTypeOfAction(actions.MOVING); setTypeOfDrawing(0); }} >Move Node</button>
            <button onClick={() => { setTypeOfAction(actions.ERASING); setTypeOfDrawing(0); }} >Remove Node</button>
            <button onClick={() => { setTypeOfAction(actions.ERASING); setTypeOfDrawing(1); }} >Remove Edge</button>
        </>
    );
};

export default Display;