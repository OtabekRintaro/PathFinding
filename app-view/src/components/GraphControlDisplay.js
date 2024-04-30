

const GraphControlDisplay = (props) => {

    const [addNodeMutation, clearGraphMutation] = [...props.mutations];
    const setAction = props.setAction;
    const informUserAboutInstruction = props.informUserAboutInstruction;
    const clearInstructions = props.clearInstructions;

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

    return (
        <div>
            <button onClick={clearGraph}>Clear Graph</button>
            <button onClick={addNode}>Add Node</button>
            <button onClick={startAddEdge}>Add Edge</button>
            <button onClick={startRemoveNode}>Remove Node</button>
            <button onClick={startRemoveEdge}>Remove Edge</button>
            <button onClick={clearAction}>Cancel</button>
        </div>
    );
}


export default GraphControlDisplay;