// File: server.js
const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const path = require('path');
const app = express();
const server = http.createServer(app);

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Create WebSocket server
const wss = new WebSocket.Server({ server });

// Connect to Python backend WebSocket server
const backendWs = new WebSocket('ws://localhost:8765');

// Handle WebSocket connections from frontend
wss.on('connection', (ws) => {
    console.log('Frontend client connected');

    // Forward messages from frontend to backend
    ws.on('message', (message) => {
        if (backendWs.readyState === WebSocket.OPEN) {
            backendWs.send(message);
        }
    });

    // Forward messages from backend to frontend
    backendWs.on('message', (message) => {
        if (ws.readyState === WebSocket.OPEN) {
            ws.send(message);
        }
    });

    // Handle connection close
    ws.on('close', () => {
        console.log('Frontend client disconnected');
    });
});

// Handle backend WebSocket connection
backendWs.on('open', () => {
    console.log('Connected to Python backend');
});

backendWs.on('error', (error) => {
    console.error('Backend WebSocket error:', error);
});

backendWs.on('close', () => {
    console.log('Disconnected from Python backend');
    // Attempt to reconnect after 5 seconds
    setTimeout(() => {
        console.log('Attempting to reconnect to backend...');
        backendWs.connect('ws://localhost:8765');
    }, 5000);
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
    console.log(`Open http://localhost:${PORT} in your browser`);
});