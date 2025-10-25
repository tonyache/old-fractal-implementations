// --- New Drawing Function ---

function drawBifurcationDiagram(dataPoints) {
    const canvas = document.getElementById('bifurcationCanvas');
    if (!canvas) {
        console.error("Canvas element not found!");
        return;
    }
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;

    // Clear the canvas
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, width, height);

    // Set color for the plot points
    ctx.fillStyle = 'black'; // The points will be black
    
    // Size of the point (a single pixel is usually best for a dense plot)
    const POINT_SIZE = 1; 

    // Scaling factors
    // R is mapped from [R_MIN, R_MAX] to [0, width]
    // X is mapped from [0, 1] to [height, 0] (y-axis is inverted in canvas)
    const rRange = R_MAX - R_MIN;

    // Iterate through all the calculated points and plot them
    for (const point of dataPoints) {
        // Calculate X position: map r from R_MIN..R_MAX to 0..width
        const plotX = (point.r - R_MIN) / rRange * width;

        // Calculate Y position: map x from 0..1 to height..0 (inverted)
        // Note: x values are between 0 and 1 for the logistic map
        const plotY = height * (1 - point.x); 

        // Draw a single point (or small square)
        ctx.fillRect(plotX, plotY, POINT_SIZE, POINT_SIZE);
    }
    
    // Optional: Draw axes and labels for better clarity
    drawAxes(ctx, width, height);
}

// Optional helper function to draw simple axes
function drawAxes(ctx, width, height) {
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;

    // X-Axis (r) line at the bottom
    ctx.beginPath();
    ctx.moveTo(0, height);
    ctx.lineTo(width, height);
    ctx.stroke();

    // Y-Axis (x) line on the left
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(0, height);
    ctx.stroke();

    // Add labels (text)
    ctx.fillStyle = '#333';
    ctx.font = '12px Arial';
    ctx.fillText(`r = ${R_MIN}`, 10, height - 10);
    ctx.fillText(`r = ${R_MAX}`, width - 50, height - 10);
    ctx.fillText('x = 1.0', 10, 20);
    ctx.fillText('x = 0.0', 10, height - 20);
}
