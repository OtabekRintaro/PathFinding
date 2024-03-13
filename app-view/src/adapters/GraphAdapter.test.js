import GraphAdapter from './GraphAdapter'


describe('test Graph Adapter', () => {
    jest.mock('./GraphAdapter');

    const graph_adapter = new GraphAdapter();
    
    beforeAll(() => {
        jest.spyOn(GraphAdapter.prototype, 'send_request').mockImplementation((method, endpoint, data) =>{
            return null;
        } 
        );
    });

    afterAll(() => {
        jest.restoreAllMocks();
    });

    function expect_single_call_of_mock(method, endpoint){
        expect(graph_adapter.send_request.mock.calls).toHaveLength(1);

        expect(graph_adapter.send_request.mock.calls[0][0]).toBe(method);

        expect(graph_adapter.send_request.mock.calls[0][1]).toBe(endpoint);
    }

    test('Clearing the graph', () => {
        graph_adapter.clear_graph();

        expect_single_call_of_mock('DELETE', '/graph');
    });

    test('getting nodes', () => {
        graph_adapter.get_nodes();

        expect_single_call_of_mock('GET', '/nodes');
    });

    test('adding the node', () => {
        graph_adapter.add_node();

        expect_single_call_of_mock('POST', '/node');
    });

    test('removing the node', () => {
        graph_adapter.remove_node(1);

        expect_single_call_of_mock('DELETE', '/node/1');
    });

    test('adding the edge', () => {
        graph_adapter.add_edge(1,2);

        expect_single_call_of_mock('POST', '/edges/1/2');
    });

    test('removing the edge', () => {
        graph_adapter.remove_edge(1,2);

        expect_single_call_of_mock('DELETE', '/edges/1/2');
    });
});