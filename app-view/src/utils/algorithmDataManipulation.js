const algorithmDataManipulation = ({action, setAction, sourceRef, targetRef, informUserAboutInstruction}) => {
    const handleDoubleClickNode = (nodeId, node) => {
      console.log(`Double clicked node ${nodeId} in position (${node.x}, ${node.y})`);
      switch(action)
      {
        case 'SELECT_SOURCE':
            informUserAboutInstruction(`You have selected node ${nodeId} as a Source!`);
            sourceRef.current.value = nodeId;
            setAction('DO_NOTHING');
            break;
        case 'SELECT_TARGET':
            informUserAboutInstruction(`You have selected node ${nodeId} as a Target!`);
            targetRef.current.value = nodeId;
            setAction('DO_NOTHING');
            break;
        default:
            console.log(`Undefined command ${action}! Executing default behaviour - do nothing!`);
            break;
      }
    }

    return [handleDoubleClickNode];
};

export default algorithmDataManipulation;