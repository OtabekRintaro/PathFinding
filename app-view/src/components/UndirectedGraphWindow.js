import GraphWindow from './GraphWindow';

const UndirectedGraphWindow = ({ graph_query, config }) => {
    config['directed'] = false;

    return (
        <div className="text-bg-dark d-flex justify-content-center">
            <GraphWindow 
                graph_query={graph_query}
                config={config}
            />
        </div>
    );
};

export default UndirectedGraphWindow;