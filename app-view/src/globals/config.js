const config = {
  "automaticRearrangeAfterDropNode": true,
  "collapsible": false,
  "directed": false,
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
    "alphaTarget": 0.50,
    "gravity": -250,
    "linkLength": 120,
    "linkStrength": 2,
    "disableLinkForce": false
  },
  "node": {
    "color": "black",
    "fontColor": "white",
    "fontSize": 15,
    "fontWeight": "normal",
    "highlightColor": "black",
    "highlightFontSize": 15,
    "highlightFontWeight": "white",
    "highlightStrokeColor": "red",
    "highlightStrokeWidth": 1.5,
    "labelPosition": "top",
    "mouseCursor": "pointer",
    "opacity": 0.9,
    "renderLabel": true,
    "size": 500,
    "strokeColor": "#d3d3d3",
    "strokeWidth": 1.0,
    "svg": "",
    "symbolType": "circle",
    "viewGenerator": null
  },
  "link": {
    "color": "lightgray",
    "fontColor": "white",
    "fontSize": 13,
    "fontWeight": "normal",
    "highlightColor": "red",
    "highlightFontSize": 13,
    "highlightFontWeight": "normal",
    "labelProperty": "label",
    "mouseCursor": "pointer",
    "opacity": 1,
    "renderLabel": true,
    "semanticStrokeWidth": true,
    "strokeWidth": 2,
    "markerHeight": 6,
    "markerWidth": 6,
    "type": "STRAIGHT",
    "selfLinkDirection": "TOP_RIGHT",
    "strokeDasharray": 0,
    "strokeDashoffset": 0,
    "strokeLinecap": "butt"
  }
};

export default config;