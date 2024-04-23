import { useEffect } from 'react';
import Drawing from "../utils/Drawing.js";

export const useClearCanvas = (ref, deps) => {
    useEffect(() =>{
        if(ref?.current)
        {
            const ctx = ref.current.getContext("2d");
            const drawing = new Drawing(ctx, 1000, 500);

            drawing.clearCanvas();
        }
    }, [deps]);
}