import { useMutation } from '@tanstack/react-query';
import { add_node, add_edge, clear_graph, remove_node, remove_edge } from "../adapters/GraphAdapter.js";

const useMutationsForGraph = ({queryClient}) => {
    const clearGraphMutation = useMutation({
        mutationFn: clear_graph,
        onSuccess: () => {
          queryClient.invalidateQueries(['graph']);
        },
    });
    
    const addNodeMutation = useMutation({
        mutationFn: add_node,
        onSuccess: () => {
            queryClient.invalidateQueries(['graph']);
        },
    });

    const addEdgeMutation = useMutation({
        mutationFn: add_edge,
        onSuccess: () => {
            queryClient.invalidateQueries(['graph']);
        },
    });

    const removeNodeMutation = useMutation({
        mutationFn: remove_node,
        onSuccess: () => {
            queryClient.invalidateQueries(['graph'])
        },
    });

    const removeEdgeMutation = useMutation({
        mutationFn: remove_edge,
        onSuccess: () => {
            queryClient.invalidateQueries(['graph'])
        },
    });

    return [clearGraphMutation, addNodeMutation, addEdgeMutation, removeNodeMutation, removeEdgeMutation];
};

export default useMutationsForGraph;