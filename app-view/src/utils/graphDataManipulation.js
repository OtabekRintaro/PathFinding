import { NON_SELECTED } from "../globals/globalVars.js";

const graphDataManipulation = ({action, setAction, selectedId, setSelectedId, addEdgeMutation, removeNodeMutation, removeEdgeMutation, informUserAboutInstruction}) => {

    const removeNode = async (node_id) => {
      removeNodeMutation.mutate(node_id);
    };
  
    const removeEdge = async ([node_id1, node_id2]) => {
      removeEdgeMutation.mutate([node_id1, node_id2]);
    };
  
    const addEdge = async ([node_id1, node_id2]) => {
      addEdgeMutation.mutate([selectedId, node_id2]);
    }
    
    const clearInstructions = () => {
        informUserAboutInstruction('');
    }

    const handleClickNode = (nodeId, node) => {
      console.log(`Clicked node ${nodeId} in position (${node.x}, ${node.y})`);
      switch(action)
      {
        case 'ADD_EDGE':
          if(selectedId === NON_SELECTED)
          {
            informUserAboutInstruction(`You have selected node ${nodeId}, choose the second node to link!`);
            setSelectedId(nodeId);
          }
          else 
          {
            informUserAboutInstruction(`You have connected nodes ${selectedId} and ${nodeId}!`);
            setTimeout(clearInstructions,5000);
            addEdge([selectedId, nodeId]);
            setAction('');
            setSelectedId(NON_SELECTED);
          }
          break;
        case 'REM_NODE':
          informUserAboutInstruction(`You have deleted node ${nodeId}! Reindexing nodes (ids > ${nodeId} are decreased by one)!`);
          removeNode(nodeId);
          break;
        default:
          console.log(`Undefined command ${action}! Executing default behaviour - do nothing!`);
          break;
      }
    }
  
    const handleClickLink = (source, target) => {
      switch(action){
        case 'REM_EDGE':
          informUserAboutInstruction(`You have deleted edge between ${source} and ${target}!`);
          removeEdge([source, target]);
          break;
        default:
          console.log(`Undefined command ${action}! Executing default behaviour - do nothing!`);
          break;
      }
    };

    return [handleClickNode, handleClickLink];
};

export default graphDataManipulation;