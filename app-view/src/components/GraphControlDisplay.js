import { useMutation } from "@tanstack/react-query";
import { set_ready_graph } from "../adapters/GraphAdapter";
import { useRef } from "react";
import Button from 'react-bootstrap/Button';
import ButtonToolbar from 'react-bootstrap/ButtonToolbar';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import InputGroup from 'react-bootstrap/InputGroup';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';

const GraphControlDisplay = (props) => {
    const selectRef = useRef(null);
    const [addNodeMutation, clearGraphMutation] = [...props.mutations];
    const action = props.action;
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
        setAction('DO_NOTHING');
        addNodeMutation.mutate();
    }

    const startAddEdge = (event) => {
        informUserAboutInstruction('To add edge - press the nodes you want to link!');
        setAction('ADD_EDGE');
    };

    const startSetWeight = () => {
        informUserAboutInstruction('To set the weight of the edge, click on it!');
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
            <ButtonToolbar className="mb-3" aria-label="Toolbar of Graph manipulation">
                <ButtonGroup className="me-2" aria-label="Node manipulation">
                    <Button variant="outline-light" onClick={addNode}>Add Node</Button>{' '}
                    <Button variant="outline-light" onClick={startRemoveNode}>Remove Node</Button>
                </ButtonGroup>
                <ButtonGroup className="me-2" aria-label="Edge manipulation">
                    <Button variant="outline-light" onClick={startAddEdge}>Add Edge</Button>
                    <Button variant="outline-light" onClick={startRemoveEdge}>Remove Edge</Button>
                </ButtonGroup>
            </ButtonToolbar>
            <ButtonToolbar className="mb-3" aria-label="Toolbar for Graph Manipulation - Second Row">
                <Col horizontal xs={6}>
                    <InputGroup>
                        <InputGroup.Text className="bg-dark text-white" id="btnGroupAddon">Weight</InputGroup.Text>
                        <Form.Control className="bg-dark text-white" ref={weightRef} id='weight' type='number' onClick={handleWeightClick} onChange={handleWeightChange}/>
                        <Button variant="outline-light" onClick={startSetWeight}>Set Weight</Button>
                    </InputGroup>
                </Col>
            </ButtonToolbar>
            <ButtonToolbar className="mb-3">
                <Form.Select aria-label="Graph selector" ref={selectRef} id="graph" onChange={handleGraphChange}>
                    <option value="custom">Select Custom Graph</option>
                    <option value="5">Binary Tree</option>
                    <option value="6">Unweighted Sparse Graph 1</option>
                    <option value="7">Unweighted Sparse Graph 2</option>
                    <option value="8">Weighted Network Graph 1</option>
                    <option value="9">Weighted Network Graph 2</option>
                    <option value="10">Weighted Network Graph (Negative Weights)</option>
                </Form.Select>
            </ButtonToolbar>
            <ButtonToolbar className="mb-3" aria-label="Toolbar of Graph manipulation">
                <ButtonGroup className="me-2" aria-label="Clearing Graph">
                    <Button variant="outline-light" onClick={clearGraph}>Clear Graph</Button>
                </ButtonGroup>
                <ButtonGroup className="me-2" aria-label="Canceling Current Action">
                {action !== 'DO_NOTHING' && action !== '' ? 
                    <Button variant="outline-danger" onClick={clearAction}>Cancel Current Action</Button>
                        : null }
                </ButtonGroup>
            </ButtonToolbar>
        </>
    );
}


export default GraphControlDisplay;