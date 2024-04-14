
class Drawing{
    constructor(ctx, ctx_width, ctx_height){
        this.ctx = ctx;
        this.width = ctx_width;
        this.height = ctx_height;
    }

    drawCircle(radius,
               lineWidth,
               strokeStyle, 
               colorFill, 
               startY, 
               startX){
        this.ctx.lineWidth = lineWidth;
        this.ctx.strokeStyle = strokeStyle;
        
        this.ctx?.beginPath();
        // console.log("Drawing circle, starting(center) points", startX, startY);
        this.ctx?.arc(startX, startY, radius, 0, Math.PI * 2, true);
        this.ctx?.stroke();
        if (colorFill) {
            this.ctx.fillStyle = colorFill;
            this.ctx.fill();
        }
    }

    drawEdge(lineWidth,
             strokeStyle,
             startX,
             startY,
             endX,
             endY){
        this.ctx.lineWidth = lineWidth;
        this.ctx.strokeStyle = strokeStyle;
        
        this.ctx?.beginPath(); 
        console.log("Drawing edge, starting points", startX, startY, " end points ", endX, endY);
        this.ctx?.moveTo(startX, startY);
        this.ctx?.lineTo(endX, endY);
        this.ctx?.closePath();
        this.ctx?.stroke();
    }

    clearCanvas(){
        this.ctx?.clearRect(0, 0, this.width, this.height);
    }

}

export default Drawing;