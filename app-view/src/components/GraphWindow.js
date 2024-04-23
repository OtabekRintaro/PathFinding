import { Graph } from "react-d3-graph";
import { useQueryClient, useMutation, useQuery } from '@tanstack/react-query';
import { get_graph, add_node } from "../adapters/GraphAdapter.js";


const GraphWindow = () => {
  const queryClient = useQueryClient();

  const graph_query = useQuery({
    queryKey: ['graph'],
    queryFn: get_graph
  });
  
  console.log(JSON.parse(JSON.stringify(graph_query)));
  let temp_data = {nodes: [], links: []};
  if(graph_query.isSuccess)
  {
    const take_data = (data_object) => {
      let data_for_graph = {'nodes': [], 'links': []};
      let nodes_for_graph = [];
      const nodes = data_object['graph']['nodes'];
      // const links = data_object['graph']['edges'];
      
      if(nodes)
      {
        console.log(data_object['graph']['nodes']);
        for(const node in nodes)
        {
          nodes_for_graph.push({'id': node})
        }
        console.log(nodes_for_graph);
        data_for_graph['nodes'] = nodes_for_graph;
      }
      return data_for_graph;
    };
  
    temp_data = take_data(graph_query.data);
    console.log(temp_data);
  }

  const data = temp_data;

  const addNodeMutation = useMutation({
    mutationFn: add_node,
    onSuccess: () => {
      queryClient.invalidateQueries({queryKey: ['graph']});
    }
  });

  const addNode = async (event) => {
    addNodeMutation.mutate();
  }


  const myConfig = {
    "automaticRearrangeAfterDropNode": true,
    "collapsible": true,
    "directed": true,
    "focusAnimationDuration": 0.75,
    "focusZoom": 1,
    "freezeAllDragEvents": false,
    "height": 400,
    "highlightDegree": 2,
    "highlightOpacity": 0.2,
    "linkHighlightBehavior": true,
    "maxZoom": 12,
    "minZoom": 0.05,
    "initialZoom": null,
    "nodeHighlightBehavior": true,
    "panAndZoom": false,
    "staticGraph": false,
    "staticGraphWithDragAndDrop": false,
    "width": 800,
    "d3": {
      "alphaTarget": 0.05,
      "gravity": -250,
      "linkLength": 120,
      "linkStrength": 2,
      "disableLinkForce": false
    },
    "node": {
      "color": "#d3d3d3",
      "fontColor": "black",
      "fontSize": 10,
      "fontWeight": "normal",
      "highlightColor": "red",
      "highlightFontSize": 14,
      "highlightFontWeight": "bold",
      "highlightStrokeColor": "red",
      "highlightStrokeWidth": 1.5,
      "labelPosition": "",
      "mouseCursor": "crosshair",
      "opacity": 0.9,
      "renderLabel": true,
      "size": 200,
      "strokeColor": "none",
      "strokeWidth": 1.5,
      "svg": "",
      "symbolType": "circle",
      "viewGenerator": null
    },
    "link": {
      "color": "lightgray",
      "fontColor": "black",
      "fontSize": 8,
      "fontWeight": "normal",
      "highlightColor": "red",
      "highlightFontSize": 8,
      "highlightFontWeight": "normal",
      "labelProperty": "label",
      "mouseCursor": "pointer",
      "opacity": 1,
      "renderLabel": false,
      "semanticStrokeWidth": true,
      "strokeWidth": 3,
      "markerHeight": 6,
      "markerWidth": 6,
      "type": "STRAIGHT",
      "selfLinkDirection": "TOP_RIGHT",
      "strokeDasharray": 0,
      "strokeDashoffset": 0,
      "strokeLinecap": "butt"
    }
  };

    return (
      <>
        <Graph 
            id="graph-id"
            data={data}
            config={myConfig}
        />
        <button onClick={addNode}>Add Node</button>
        {/* <GraphControl/> */}
      </>);
};

export default GraphWindow;