import { useEffect, useState, useRef } from 'react';

export const useData = (fetchingFunction, functionParams, initialState, refetch, setRefetch) => {
    const ignore = useRef(false);
    const [data, setData] = useState(initialState);
    useEffect(() => {
        if(refetch)
        {
            fetchingFunction(functionParams)
                .then((result) => {
                    if(!ignore.current) {
                        console.log("result ", result);
                        setData(result);
                    }
                });
            setRefetch(false);
            return () => {
                ignore.current = true;
            };
        }
    }, [refetch]); 
    return [data, setData];
};