import { useRef } from "react";
import { useMutation } from '@tanstack/react-query';
import { change_alogrithm, run_algorithm, next_algorithm_step, stop_algorithm_process } from "../adapters/GraphAdapter";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import InputGroup from 'react-bootstrap/InputGroup';
import Row from "react-bootstrap/esm/Row";
import Col from "react-bootstrap/esm/Col";

const AlgorithmControlDisplay = (props) => {
    const informUserAboutInstruction = props.informUserAboutInstruction;
    const setAction = props.setAction;
    const [sourceRef, targetRef] = props.refs;
    const queryClient = props.queryClient;
    
    const selectRef = useRef(null);
    
    const runAlgorithmMutation = useMutation({
        mutationFn: run_algorithm,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
    });

    const runNextStepMutation = useMutation({
        mutationFn: next_algorithm_step,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
    });
    
    const changeAlgorithmMutation = useMutation({
        mutationFn: change_alogrithm,
        onSuccess: () => queryClient.invalidateQueries(['graph']),
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
        informUserAboutInstruction('Double-click the node you want to make a Source!');
        setAction('SELECT_SOURCE')
    };

    const handleTargetChoice = (event) => {
        informUserAboutInstruction('Double-click the node you want to make a Target!');
        setAction('SELECT_TARGET')
    };
    
    const handleRunAlgorithm = () => {
        if(sourceRef.current.value && targetRef.current.value && selectRef.current?.value !== ""){
            informUserAboutInstruction('Running Algorithm!');
            runAlgorithmMutation.mutate([sourceRef.current.value, targetRef.current.value]);
        }else{
            informUserAboutInstruction('Choose the algorithm, source and target nodes first!');
        }
    };

    const doStep = (event) => {
        console.log('starting step handling - ');
        runNextStepMutation.mutate();
    }
    
    if(runAlgorithmMutation.isSuccess){
        console.log('algorithm data - ', runAlgorithmMutation.data);
    }

    const clearAlgorithm = () => {
        console.log('Cleared complete path!');
        clearAlgorithmPath.mutate();
    }

    console.log('rendered');
    return (
        <>
            <label htmlFor="algo">Choose an Algorithm:</label>
            <Form.Select className="mb-3" ref={selectRef} id="algo" onChange={handleChange}>
                <option value="" disabled selected>Select Your Algorithm</option>
                <option value="dfs">DFS</option>
                <option value="bfs">BFS</option>
                <option value="dijkstra">Dijkstra</option>
                <option value="bellmanford">Bellman-Ford</option>
            </Form.Select>
            <Row>
                <Col>
                    <InputGroup className="mb-3">
                        <InputGroup.Text className="bg-dark text-white" id="inputGroup-sizing-sm">Source</InputGroup.Text>
                        <Form.Control className="bg-dark text-white" ref={sourceRef} id='source' type='text' readOnly={true} size={5} onClick={handleSourceChoice}/>
                    </InputGroup>
                </Col>
                <Col>
                    <InputGroup className="mb-3">
                        <InputGroup.Text className="bg-dark text-white">Target</InputGroup.Text >
                        <Form.Control className="bg-dark text-white" ref={targetRef} id='target' type='text' readOnly={true} size={5} onClick={handleTargetChoice}/>
                    </InputGroup>
                </Col>
            </Row>
            <br />
            <ButtonToolbar className="mb-3" aria-label="Toolbar for Graph Manipulation - Second Row">
                <ButtonGroup className="me-2">
                    <Button variant="outline-light" onClick={handleRunAlgorithm}>Run Algorithm</Button>
                    <Button variant="outline-light" onClick={doStep} hidden={false}>Next step</Button>
                    <Button variant="outline-light" onClick={clearAlgorithm}>Clear Complete Path</Button>
                </ButtonGroup>
            </ButtonToolbar>
        </>
    );
};

export default AlgorithmControlDisplay;