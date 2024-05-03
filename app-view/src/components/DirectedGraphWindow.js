import GraphWindow from './GraphWindow';

const UndirectedGraphWindow = ({ graph_query, config }) => {
    config['directed'] = true;

    return (
        <GraphWindow 
            graph_query={graph_query}
            config={config}
        />
    );
};

export default UndirectedGraphWindow;