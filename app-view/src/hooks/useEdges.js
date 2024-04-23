import { useEffect } from 'react';
import Drawing from "../utils/Drawing.js";

export const useEdges = (ref, edges, nodes, selected, typeOfAction, actions) => {
    useEffect(() =>{
        if(ref?.current)
        {
            const ctx = ref.current.getContext("2d");
            const drawing = new Drawing(ctx, 1000, 500);

            edges.map((edge, index) =>
                requestAnimationFrame(() => {
                    console.log(edge, index)
                    const startX = nodes[edge.from].x;
                    const startY = nodes[edge.from].y;
                    const endX = nodes[edge.to].x;
                    const endY = nodes[edge.to].y;

                    if (typeOfAction === actions.ERASING && (selected === edge.from || selected === edge.to))
                        drawing.drawEdge(1.7, "red", startX, startY, endX, endY);
                    else
                        drawing.drawEdge(1.7, "white", startX, startY, endX, endY);
                })
            )
        }
    });
}