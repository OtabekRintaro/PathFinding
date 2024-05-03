import axios from 'axios';

const SERVER_ADDRESS = 'http://192.168.0.199:5000';

export const set_graph_type = (graph_type) =>
    axios.put(SERVER_ADDRESS + '/graph/' + graph_type).then(response => response.data);

export const clear_graph = () =>
    axios.delete(SERVER_ADDRESS + '/graph').then(response => response.data);

export const get_graph = () =>
    axios.get(SERVER_ADDRESS + '/graph').then(response => response.data);

export const add_node = () =>
    axios.post(SERVER_ADDRESS + '/node').then(response => response.data);

export const remove_node = (node_id) =>
    axios.delete(SERVER_ADDRESS + '/node/' + node_id).then(response => response.data);

export const add_edge = ([node_id1, node_id2]) =>
    axios.post(SERVER_ADDRESS + '/edges/' + node_id1 + '/' + node_id2).then(response => response.data);

export const set_weight = ([node_id1, node_id2, weight]) => 
    axios.put(SERVER_ADDRESS + '/edges/' + node_id1 + '/' + node_id2 + '/' + weight).then(response => response.data)

export const remove_edge = ([node_id1, node_id2]) =>
    axios.delete(SERVER_ADDRESS + '/edges/' + node_id1 + '/' + node_id2).then(response => response.data);

export const change_alogrithm = (algorithm_name) => 
    axios.put(SERVER_ADDRESS + '/algorithm/' + algorithm_name).then(response => response.data);

export const run_algorithm = ([source, target]) => 
    axios.post(SERVER_ADDRESS + '/algorithm/' + source + '/' + target).then(response => response.data);

export const next_algorithm_step = () => 
    axios.put(SERVER_ADDRESS + '/algorithm/next_step').then(response => response.data)

export const stop_algorithm_process = () =>
    axios.delete(SERVER_ADDRESS + '/algorithm').then(response => response.data);
    