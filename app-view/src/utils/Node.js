import { useEffect, useRef, useState } from "react";
import Drawing from "./drawing.js";


const useMousePosition = (
    global = false
  ) => {
   const [mouseCoords, setMouseCoords] = useState({
      x: 0,
      y: 0
    });
  
   const handleCursorMovement = (event) => {
   let rect = event.target.getBoundingClientRect();
      setMouseCoords({
        x: event.clientX - rect.left,
        y: event.clientY - rect.top
      });
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

const Node = () => {
 const widthA = 1000;
 const canvasRef = useRef(null);
 const [radius, setRadius] = useState(15);
 const [coords, handleCoords] = useMousePosition();
 const [nodes, setNodes] = useState([])
 
  

  useEffect(() => {
    if (canvasRef?.current) {
        
        const ctx = canvasRef.current.getContext("2d");
        const drawing = new Drawing(ctx, 1000, 500);

          requestAnimationFrame(function ball() {
              drawing.drawCircle(radius, 0.7, "white", "black", coords.y, coords.x);
              ctx?.stroke();
              if(radius < 50){
                  setRadius(radius + 1.5);
              }
          });
    }
  }, [radius, nodes, coords.x, coords.y]);
 return (
    <>
      <canvas
        ref={canvasRef}
        width={widthA.toString()}
        height="350"
        style={{ border: "2px solid black" }}
        onClick={(e) => {
          handleCoords(e);
          setNodes(nodes + [{x: coords.x, y: coords.y}])
          setRadius(15);
        }}
        />
    </>
  );
};

export default Node;