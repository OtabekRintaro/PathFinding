

const ControlDisplay = (props) => {

    const [addNodeMutation, clearGraphMutation] = [...props.mutations]
    const setAction = props.setAction
    const informUserAboutInstruction = props.informUserAboutInstruction

    const addNode = async (event) => {
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

    return (
        <div>
            <button onClick={clearGraph}>Clear Graph</button>
            <button onClick={addNode}>Add Node</button>
            <button onClick={startAddEdge}>Add Edge</button>
            <button onClick={startRemoveNode}>Remove Node</button>
            <button onClick={startRemoveEdge}>Remove Edge</button>
        </div>
    );
}


export default ControlDisplay;