import { useRef } from "react";
import { useMutation } from '@tanstack/react-query';
import { change_alogrithm, run_algorithm } from "../adapters/GraphAdapter";

const AlgorithmControlDisplay = (props) => {
    const informUserAboutInstruction = props.informUserAboutInstruction;
    const clearInstructions = props.clearInstructions;
    const setAction = props.setAction;
    const [sourceRef, targetRef] = props.refs;
    const queryClient = props.queryClient;
    
    const selectRef = useRef(null);
    
    const runAlgorithmMutation = useMutation({
        mutationFn: run_algorithm,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
    });

    const changeAlgorithmMutation = useMutation({
        mutationFn: change_alogrithm
    });

    const handleChange = async (event) => {
        if(event.target.value && event.target.value !== 'dummy')
            changeAlgorithmMutation.mutate(event.target.value);
    };

    const handleSourceChoice = (event) => {
        informUserAboutInstruction('Choose the node you want to make a Source!');
        setAction('SELECT_SOURCE')
    };

    const handleTargetChoice = (event) => {
        informUserAboutInstruction('Choose the node you want to make a Target!');
        setAction('SELECT_TARGET')
    };

    const handleRunAlgorithm = () => {
        informUserAboutInstruction('Running Algorithm...');
        runAlgorithmMutation.mutate([sourceRef.current.value, targetRef.current.value]);
    };

    if(runAlgorithmMutation.isSuccess)
    {
        console.log('algorithm data - ', runAlgorithmMutation.data);
    }

    return (
        <div>
            <label htmlFor="algo">Choose an Algorithm:</label>
            <select ref={selectRef} id="algo" onChange={handleChange}>
                <option value="dfs">DFS</option>
                <option value="dummy">DUMMY</option>
            </select>
            <div>
                <label htmlFor='source'>Source:</label>
                <input ref={sourceRef} id='source' type='text' readOnly={true} size={5} onClick={handleSourceChoice}></input>
                <label htmlFor='target'>Target:</label>
                <input ref={targetRef} id='target' type='text' readOnly={true} size={5} onClick={handleTargetChoice}></input>
            </div>
            <button onClick={handleRunAlgorithm}>Run Algorithm</button>
        </div>
    );
};

export default AlgorithmControlDisplay;