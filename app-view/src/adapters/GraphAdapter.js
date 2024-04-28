import axios from 'axios';

const SERVER_ADDRESS = 'http://192.168.0.199:5000';

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

export const remove_edge = ([node_id1, node_id2]) =>
    axios.delete(SERVER_ADDRESS + '/edges/' + node_id1 + '/' + node_id2).then(response => response.data);
