import { useRef, useState } from "react";
import { useMutation } from '@tanstack/react-query';
import { change_alogrithm, run_algorithm, next_algorithm_step, stop_algorithm_process } from "../adapters/GraphAdapter";

const AlgorithmControlDisplay = (props) => {
    const informUserAboutInstruction = props.informUserAboutInstruction;
    const clearInstructions = props.clearInstructions;
    const setAction = props.setAction;
    const data = props.data;
    const setData = props.setData;
    const [sourceRef, targetRef, graphRef, graphWindowRef] = props.refs;
    const queryClient = props.queryClient;
    
    const algorithmStepRef = useRef(null);
    const selectRef = useRef(null);
    const runAlgorithmRef = useRef(null);
    
    const runAlgorithmMutation = useMutation({
        mutationFn: run_algorithm,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
    });

    const runNextStepMutation = useMutation({
        mutationFn: next_algorithm_step,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
    });
    
    const changeAlgorithmMutation = useMutation({
        mutationFn: change_alogrithm
    });

    const clearAlgorithmPath = useMutation({
        mutationFn: stop_algorithm_process,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
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
        if(sourceRef.current.value && targetRef.current.value){
            informUserAboutInstruction('Running Algorithm...');
            runAlgorithmMutation.mutate([sourceRef.current.value, targetRef.current.value]);
        }else{
            informUserAboutInstruction('Choose the source and target nodes first!');
            clearInstructions(5000);
        }
    };

    const doStep = (event) => {
        console.log('starting step handling - ');

        algorithmStepRef.hidden = false;
        runNextStepMutation.mutate();
    }
    
    if(runAlgorithmMutation.isSuccess){
        console.log('algorithm data - ', runAlgorithmMutation.data);
    }

    const clearAlgorithm = () => {
        console.log('Cleard complete path!');
        clearInstructions(5000);
        clearAlgorithmPath.mutate();
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
            <button ref={runAlgorithmRef} onClick={handleRunAlgorithm}>Run Algorithm</button>
            <button ref={algorithmStepRef} onClick={doStep} hidden={false}>Next step</button>
            <button onClick={clearAlgorithm}>Clear Complete Path</button>
        </div>
    );
};

export default AlgorithmControlDisplay;