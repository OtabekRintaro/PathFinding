import config from "../globals/config";
import { RUNNING_STATE, FINISHED_STATE } from "../globals/globalVars";

export const takeDataFromResponse = (data_object) => {
    let data_for_graph = {'nodes': [], 'links': []};
    const nodes = data_object['graph']['nodes'];
    const links = data_object['graph']['edges'];
    const algorithm = data_object?.algorithm;
    
    
    if(nodes)
    {
      console.log("retrieved nodes ", data_object['graph']['nodes']);
      
      const nodes_for_graph = get_nodes(nodes, links);
      
      console.log(nodes_for_graph);
      data_for_graph['nodes'] = nodes_for_graph;
    }
    if(links)
    {
      console.log("retrieved edges ",data_object['graph']['edges']);
      
      const links_for_graph = get_links(links);
      
      data_for_graph['links'] = links_for_graph;
    }

    if(algorithm)
    {
      const currentState = algorithm?.currentState;
      if(currentState && currentState === FINISHED_STATE)
      {
        const path = algorithm.path;
        if(path.length > 0){
          console.log('Full Complete Path - ', path);
          data_for_graph.nodes.forEach(node => {if(path.includes(Number(node.id))) node.color = 'green';});
          data_for_graph.nodes[path[0]].color = '#00D9A6';
          data_for_graph.nodes[path[path.length - 1]].color = '#00D9A6';
        }else{
          console.log('Path has not been found!');
        }
      }
      else if(currentState && currentState === RUNNING_STATE)
      {
        const isBellmanFord = algorithm?.isBellmanFord;
        if(isBellmanFord){
          const links = algorithm.links;
          console.log('All Links - ', links);
          const [currentHighlightedSource, currentHighlightedTarget] = links[algorithm.currentLink];
          console.log('current edge to highlight - ', currentHighlightedSource, currentHighlightedTarget);
          const link_to_highlight = data_for_graph.links.filter(link => {
            console.log('link',link);
            return link.source === currentHighlightedSource.toString() && link.target === currentHighlightedTarget.toString();
          });
           
          console.log('link_to_highlight ',link_to_highlight);
          link_to_highlight.forEach(link => link.color = 'yellow');
        }else{
          const steps = algorithm.steps;
          console.log('All Steps - ', steps);
          const currentHighlightedNodeId = steps[algorithm.currentStep];
          const visitedNodes = [] 
          for(let i = 0; i < algorithm.currentStep; i++)
          {
            visitedNodes.push(steps[i]);
          }
          data_for_graph.nodes[currentHighlightedNodeId].color = 'yellow';
          data_for_graph.nodes.forEach(node => {if(visitedNodes.includes(Number(node.id))) node.color = 'grey';} )
        }
      } 
    }

    return data_for_graph;
  };
  
  const node_not_in_links = (node, links) => {
    const linksWithNode = Object.entries(links).filter( link => {
      let [, inNodes] = link;
      return inNodes.filter(inNode => inNode[0] === node).length > 0;
    });
    return linksWithNode.length === 0;
  };

  const get_nodes = (nodes, links) => {
    let nodes_for_graph = []
    const limitHeight = config['height'] - 100;
    const limitWidth = config['width'] - 100;
    let initialX = 50;
    let initialY = 50;

    nodes.forEach(node => {
      if(node_not_in_links(node, links))
      {
        nodes_for_graph.push({'id': node.toString() , 'x': Math.floor(Math.random() * 500), 'y': Math.floor(Math.random() * 500)});
        if(initialX + 15 >= limitWidth)
          initialY = ((initialY + 10) % limitHeight) + 50;
        initialX = ((initialX + 10) % limitWidth) + 50;
      }else{
        nodes_for_graph.push({'id': node.toString()})
      }
      
    });

    return nodes_for_graph;
  }

  const get_links = (links) => {
    let links_for_graph = [];
    Object.entries(links).forEach(edge => {
      const [outNode, inNodes] = edge;
      inNodes.forEach(inNode => {
        if(inNode[0].toString() !== outNode){
          links_for_graph.push({"source": outNode, "target": inNode[0].toString(), 
          "label": (links[inNode[0]].map(node => node[0]).includes(Number(outNode)) && inNode[1] === links[inNode[0]].filter(node => node[0] === Number(outNode))[0][1] && inNode[0] > Number(outNode)) 
          ? (inNode[1] !== 0 ? inNode[1].toString() : '') : (
          (links[inNode[0]].map(node => node[0]).includes(Number(outNode)) && inNode[1] === links[inNode[0]].filter(node => node[0] === Number(outNode))[0][1]) 
          ? '' : (inNode[1] !== 0 ? inNode[1].toString() : ''))});
        }
      });
    })
    return links_for_graph;
  }