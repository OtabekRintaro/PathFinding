import Component from "react";

class Field extends Component {
    constructor(props){
        super(props);
    }
    
    render(){
        return (
            <canvas {... this.props} />
        );
    }
}

export default Field;