import { useEffect } from 'react';
import Drawing from "../utils/Drawing.js";

export const usePopOutNodes = (ref, nodes, selected, radius, setRadius, nodeRadiusBoundary) => {
    useEffect(() =>{
        console.log(1);
        // if(ref?.current)
        // {
        //     const ctx = ref.current.getContext("2d");
        //     const drawing = new Drawing(ctx, 1000, 500);
    
        //     let frameId = null;
    
        //     const onFrame = () => {
        //         const newRadiuses = radius.map((rad) => Math.min(rad + 0.5, nodeRadiusBoundary));
        //         onProgress(newRadiuses);
    
        //         nodes.map((node, index) => {
        //             console.log('frame requested', node, radius[index]);
        //                 if (index === selected)
        //                     drawing.drawCircle(radius[index], 1.7, "white", "blue", node.y, node.x);
        //                 else
        //                     drawing.drawCircle(radius[index], 1.7, "white", "black", node.y, node.x);
        //         });
    
        //         console.log(newRadiuses);
        //     }
    
        //     const onProgress = (newRadiuses) => {
        //         setRadius(newRadiuses);
        //     }
          
        //     const start = () => {
        //         onProgress([]);
        //         frameId = requestAnimationFrame(onFrame);
        //     }
          
        //     const stop = () => {
        //         cancelAnimationFrame(frameId);
        //         frameId = null;
        //     }
        //     start();
        //     return () => stop();
        // }
    }, []);
}
