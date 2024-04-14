import { useEffect, useRef, useState } from "react";
import Drawing from "./utils/drawing.js";


const useMousePosition = (
    global = false
) => {
    const [mouseCoords, setMouseCoords] = useState({
        x: -500,
        y: -500
    });

    const handleCursorMovement = (event) => {
        let rect = event.target.getBoundingClientRect();
        const newX = event.clientX - rect.left;
        const newY = event.clientY - rect.top;
        setMouseCoords({
            x: event.clientX - rect.left,
            y: event.clientY - rect.top
        });
        return [newX, newY];
    };
    useEffect(() => {
        if (global) {
            window.addEventListener("mousemove", handleCursorMovement);

            return () => {
                window.removeEventListener("mousemove", handleCursorMovement);
            };
        }
    }, [global]);

    return [mouseCoords, handleCursorMovement];
};

const Display = () => {
    const widthA = 1000;
    const canvasRef = useRef(null);
    const NON_SELECTED = -1;
    const nodeRadiusBoundary = 25;
    const typesOfDrawing = ['circle', 'undirected_edge', 'directed_edge']
    const [radius, setRadius] = useState([]);
    const [coords, handleCoords] = useMousePosition();
    const [nodes, setNodes] = useState([])
    const [edges, setEdges] = useState([])
    const [typeOfDrawing, setTypeOfDrawing] = useState(0)
    const [selected, setSelected] = useState(NON_SELECTED)

    const isNode = (coordinates) => {
        console.log("checking if ", coordinates.x, coordinates.y, " are in nodes");
        const x = coordinates.x;
        const y = coordinates.y;

        let index_of_node = undefined;

        nodes.map( (node, index) => {
            console.log("is node iteration ", node.x, node.y)
            const dx = Math.abs(x - node.x);
            if (dx <= nodeRadiusBoundary)
            {
                const dy = Math.abs(y - node.y);
                if (dy <= nodeRadiusBoundary)
                {
                    console.log("dist from the center", dx, dy);
                    if (dx*dx + dy*dy <= nodeRadiusBoundary*nodeRadiusBoundary)
                        index_of_node = index;
                }
            }
        });

        return index_of_node;
    } 

    useEffect(() => {
        if (canvasRef?.current) {
            const ctx = canvasRef.current.getContext("2d");
            const drawing = new Drawing(ctx, 1000, 500);

            drawing.clearCanvas();
            edges.map( (edge, index) => {
                requestAnimationFrame(() => {
                    console.log(edge)
                    const startX = nodes[edge.from].x;
                    const startY = nodes[edge.from].y;
                    const endX = nodes[edge.to].x;
                    const endY = nodes[edge.to].y;

                    drawing.drawEdge(0.7, "white", startX, startY, endX, endY);
                });
            });

            nodes.map((node, index) => {
                requestAnimationFrame(() => {
                    drawing.drawCircle(radius[index], 0.7, "white", "black", node.y, node.x);
                    if (radius[index] < nodeRadiusBoundary) {
                        let newRadius = radius;
                        newRadius[index] += 0.5;
                        setRadius([ ...newRadius]);
                    }
                });   
            });

        }
    }, [radius, edges, nodes, coords.x, coords.y]);

    return (
        <>
            <canvas
                ref={canvasRef}
                width={widthA.toString()}
                height="550"
                style={{ border: "2px solid black" }}
                onClick={(e) => {
                    const [newX, newY] = handleCoords(e);
                    if(typeOfDrawing === 0){
                        setNodes(nodes.concat([{ x: newX, y: newY }]));
                        setRadius(radius.concat([15])); 
                    }else if(typeOfDrawing === 1)
                    {
                        const newPoint = { x: newX, y: newY }
                        const current_node_index = isNode(newPoint);

                        console.log("current node index", current_node_index);

                        if(selected === -1)
                        {
                            if(current_node_index > -1){
                                console.log("new first node", current_node_index);
                                setSelected(current_node_index);
                            }
                        }else{
                            if(current_node_index)
                                setEdges(edges.concat([{ from: selected, to: current_node_index }]));
                            setSelected(NON_SELECTED);
                        }
                        
                    }
                }}
            />
            <button onClick={() => setTypeOfDrawing(0)} >Nodes</button>
            <button onClick={() => setTypeOfDrawing(1)} >Edges</button>
        </>
    );
};

export default Display;