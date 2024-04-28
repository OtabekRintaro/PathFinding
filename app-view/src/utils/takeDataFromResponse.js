import config from "../globals/config";

export const takeDataFromResponse = (data_object) => {
    let data_for_graph = {'nodes': [], 'links': []};
    let nodes_for_graph = [];
    let links_for_graph = [];
    const nodes = data_object['graph']['nodes'];
    const links = data_object['graph']['edges'];
    
    if(nodes)
    {
      console.log("retrieved nodes ", data_object['graph']['nodes']);
      const limitHeight = config['height'] - 100;
      const limitWidth = config['width'] - 100;
      let initialX = 50;
      let initialY = 50;
      nodes.forEach(node => {
        nodes_for_graph.push({'id': node.toString(), 'x': initialX, 'y': initialY});
        if(initialX + 15 >= limitWidth)
          initialY = ((initialY + 10) % limitHeight) + 50;
        initialX = ((initialX + 10) % limitWidth) + 50;
      });
      console.log(nodes_for_graph);
      data_for_graph['nodes'] = nodes_for_graph;
    }
    if(links)
    {
      console.log("retrieved edges ",data_object['graph']['edges']);
      Object.entries(links).forEach(edge => {
        const [outNode, inNodes] = edge;
        inNodes.forEach(inNode => links_for_graph.push({"source": outNode, "target": inNode.toString()}));
      })
      data_for_graph['links'] = links_for_graph;
    }
    return data_for_graph;
  };