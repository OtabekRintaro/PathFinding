import { useEffect, useState } from "react";

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

export default useMousePosition;