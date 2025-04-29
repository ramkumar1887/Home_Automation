# Home Automation System

A modern home automation system with a web-based control interface and Python backend. The system allows you to control various smart devices including thermostat, lights, security camera, smart lock, and motion sensors.

## Project Structure

```
home_automation/
├── public/
│   └── index.html      # Frontend web interface
├── server.js           # Node.js WebSocket bridge
├── backend/
│   └── nw.py          # Python WebSocket server
└── README.md
```

## Components

1. **Frontend (Web Interface)**
   - Built with HTML, CSS, and JavaScript
   - Real-time device status monitoring
   - Interactive controls for all devices
   - Responsive design for all screen sizes

2. **WebSocket Bridge (server.js)**
   - Node.js application using Express and WebSocket
   - Acts as a bridge between frontend and backend
   - Handles WebSocket connections and message routing
   - Serves static files for the web interface

3. **Backend (nw.py)**
   - Python WebSocket server
   - Manages device states and commands
   - Handles device communication
   - Implements business logic for device control

## Features

- Real-time device status updates
- Temperature control for thermostat
- Light brightness adjustment
- Security camera live feed and recording
- Smart lock control and access logs
- Motion sensor monitoring
- Automatic reconnection handling
- Responsive web interface

## Prerequisites

- Node.js (v14 or higher)
- Python 3.7 or higher
- npm (Node Package Manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ramkumar1887/Home_Automation.git
   cd home_automation
   ```

2. Install Node.js dependencies:
   ```bash
   npm install express ws
   ```

3. Install Python dependencies:
   ```bash
   pip install websockets
   ```

## Running the Application

1. Start the Python backend:
   ```bash
   cd backend
   python nw.py
   ```

2. In a new terminal, start the Node.js bridge:
   ```bash
   node server.js
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:3000
   ```

## Development

### Frontend Development
- The frontend is built with vanilla HTML, CSS, and JavaScript
- All frontend files are located in the `public` directory
- The main interface is in `index.html`

### Backend Development
- The backend is written in Python using the `websockets` library
- Device states and logic are managed in `nw.py`
- WebSocket communication is handled on port 8765

### Bridge Development
- The bridge is written in Node.js using Express and WebSocket
- It runs on port 3000 by default
- Handles WebSocket connections between frontend and backend

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
