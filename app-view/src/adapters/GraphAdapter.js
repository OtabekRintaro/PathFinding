import axios from 'axios';

const SERVER_ADDRESS = 'http://localhost:5000';

class GraphAdapter{

    constructor(){
        this.client = axios.create({
            baseURL: SERVER_ADDRESS,
            json: true
        });
    }

    clear_graph(){
        return this.send_request('DELETE', '/graph');
    }

    get_nodes(){
        return this.send_request('GET', '/nodes');
    };

    add_node(){
        return this.send_request('POST', '/node');
    };

    remove_node(node_id){
        return this.send_request('DELETE', '/node/' + node_id.toString());
    }

    add_edge(node_id1, node_id2){
        return this.send_request('POST', '/edges/' + node_id1 + '/' + node_id2.toString());
    }

    remove_edge(node_id1, node_id2){
        return this.send_request('DELETE', '/edges/' + node_id1 + '/' + node_id2.toString());
    }

    async send_request(method, endpoint, data){
        return this.client({
            method,
            url: endpoint,
            data
        }).then(response => {
            return response.data ? response.data : [];
        }).catch(e => console.log(e));
    }

};

export default GraphAdapter;