import GraphWindow from './GraphWindow';

const UndirectedGraphWindow = ({ graph_query, config }) => {
    config['directed'] = false;

    return (
        <GraphWindow 
            graph_query={graph_query}
            config={config}
        />
    );
};

export default UndirectedGraphWindow;