import { Component } from "react";

class Field extends Component {
    constructor(props){
        super(props);
        this.canvasRef = useRef(null);
        useEffect(() => {
            this.canvas = canvasRef.current
            this.context = canvas.getContext('2d')
            //Our first draw
            this.context.fillStyle = '#000000'
            this.context.fillRect(0, 0, context.canvas.width, context.canvas.height)
          }, [])
    }
    
    render(){
        return (
            <canvas ref={this.canvasRef} {... this.props}></canvas>
        );
    }
}

export default Field;