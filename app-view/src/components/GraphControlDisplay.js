import { useMutation } from "@tanstack/react-query";
import { set_ready_graph } from "../adapters/GraphAdapter";
import { useRef } from "react";


const GraphControlDisplay = (props) => {
    const selectRef = useRef(null);
    const [addNodeMutation, clearGraphMutation] = [...props.mutations];
    const setAction = props.setAction;
    const informUserAboutInstruction = props.informUserAboutInstruction;
    const clearInstructions = props.clearInstructions;
    const weightRef = props.weightRef;
    const queryClient = props.queryClient;

    const setReadyGraphMutation = useMutation({
        mutationFn: set_ready_graph,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
    });

    const addNode = async (event) => {
        informUserAboutInstruction('Added node!');
        clearInstructions(5000);
        setAction('ADD_NODE');
        addNodeMutation.mutate();
    }

    const startAddEdge = (event) => {
        informUserAboutInstruction('To add edge - press the nodes you want to link!');
        setAction('ADD_EDGE');
    };

    const startSetWeight = () => {
        informUserAboutInstruction('To set the weight of the edge, double click on it!');
        setAction('SET_WEIGHT')
    }

    const startRemoveNode = () => {
        informUserAboutInstruction('To remove node - press the nodes you want to remove!');
        setAction('REM_NODE');
    };

    const startRemoveEdge = () => {
        informUserAboutInstruction('To remove edge - press the edges you want to remove!');
        setAction('REM_EDGE');
    };

    const clearGraph = async () => {
        setAction('DO_NOTHING');
        clearGraphMutation.mutate();
    };

    const clearAction = async () => {
        setAction('DO_NOTHING');
        clearInstructions();
    };

    const handleWeightClick = () => {
        informUserAboutInstruction('Write down the desired weight!');
        setAction('DO_NOTHING');
    };

    const handleWeightChange = (event) => {
        if(weightRef?.current)
            weightRef.current.value = event.target.value;
        setAction('DO_NOTHING');
    };

    const handleGraphChange = (event) => {
        if(selectRef.current && event.target.value !== 'custom'){
            console.log("Changing graph to graph - " + event.target.value);
            selectRef.current.value = event.target.value;
            setReadyGraphMutation.mutate(selectRef.current.value);
        }    
        setAction('DO_NOTHING');
    }

    console.log('rendered');
    return (
        <>
            <div>
                <button onClick={clearGraph}>Clear Graph</button>
                <button onClick={addNode}>Add Node</button>
                <button onClick={startAddEdge}>Add Edge</button>
                <input ref={weightRef} id='weight' type='number' size={5} onClick={handleWeightClick} onChange={handleWeightChange}></input>
                <button onClick={startSetWeight}>Set Weight</button>
                <button onClick={startRemoveNode}>Remove Node</button>
                <button onClick={startRemoveEdge}>Remove Edge</button>
                <button onClick={clearAction}>Cancel</button>
            </div>
            <div>
                <select ref={selectRef} id="graph" onChange={handleGraphChange}>
                    <option value="custom">Custom Graph</option>
                    <option value="1">Prepared Graph 1</option>
                    <option value="2">Prepared Graph 2</option>
                    <option value="3">Prepared Graph 3</option>
                </select>
            </div>
        </>
    );
}


export default GraphControlDisplay;