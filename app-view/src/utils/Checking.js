const placeIsFree = (nodes, x, y, nodeRadiusBoundary) => {
    return nodes.length === 0 || isNode(nodes, { x: x, y: y }, nodeRadiusBoundary * 2) === undefined;
};

const canConnect = ( edges, selected, index ) => {
    return uniqueEdgeTo( edges, selected, index ) && index !== selected;
};

const uniqueEdgeTo = (edges, selected, index ) => {
    console.log(edges);
    return edges.every((edge) => !(edge.from === selected && edge.to === index) 
                                 &&
                                 !(edge.to === selected && edge.from === index));
};

const isNode = (nodes, coordinates, radiusToCheck) => {
    // console.log("checking if ", coordinates.x, coordinates.y, " are in nodes");
    const x = coordinates.x;
    const y = coordinates.y;

    let index_of_node = undefined;

    nodes.map( (node, index) => {
        // console.log("is node iteration ", node.x, node.y)
        const dx = Math.abs(x - node.x);
        if (dx <= radiusToCheck)
        {
            const dy = Math.abs(y - node.y);
            if (dy <= radiusToCheck)
            {
                // console.log("dist from the center", dx, dy);
                if (dx*dx + dy*dy <= radiusToCheck*radiusToCheck)
                    index_of_node = index;
            }
        }

        return index_of_node;
    });

    return index_of_node;
} 

const newArrayWithoutIndex = (arr, index) => [...arr.slice(0, index).concat(arr.slice(index + 1))];

export { placeIsFree, canConnect, isNode, newArrayWithoutIndex};