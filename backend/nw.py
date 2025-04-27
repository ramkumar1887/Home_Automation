import json
from websockets.sync.server import serve

# Device states
devices = {
    'thermostat': {'value': 22, 'mode': 'auto', 'status': 'online'},
    'light': {'value': 70, 'status': 'online'},
    'camera': {'recording': False, 'status': 'online'},
    'lock': {'locked': True, 'status': 'online'},
    'motion': {'motionDetected': False, 'lastDetected': None, 'status': 'online'}
}

def handle_command(command):
    """Process a command and update device states"""
    device = command.get('device')
    action = command.get('action')
    value = command.get('value')
    
    print(f"Received command: {command}")
    
    if device in devices:
        if device == 'thermostat':
            if action == 'set':
                devices[device]['value'] = value
            elif action == 'mode':
                devices[device]['mode'] = value
        elif device == 'light':
            if action == 'set':
                devices[device]['value'] = value
        elif device == 'camera':
            if action == 'record':
                devices[device]['recording'] = True
            elif action == 'stop':
                devices[device]['recording'] = False
        elif device == 'lock':
            if action == 'lock':
                devices[device]['locked'] = True
            elif action == 'unlock':
                devices[device]['locked'] = False
        elif device == 'motion':
            if action == 'trigger':
                devices[device]['motionDetected'] = True
                devices[device]['lastDetected'] = 'now'
    
    print(f"Updated device states: {devices}")
    return devices

def websocket_handler(websocket):
    """Handle WebSocket connections"""
    print("Client connected")
    
    try:
        # Send initial device states
        websocket.send(json.dumps({'type': 'status', 'data': devices}))
        
        # Handle incoming messages
        for message in websocket:
            try:
                command = json.loads(message)
                if command.get('type') == 'command':
                    updated_states = handle_command(command)
                    # Send confirmation with updated states
                    websocket.send(json.dumps({'type': 'status', 'data': updated_states}))
            except json.JSONDecodeError:
                print(f"Invalid JSON received: {message}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Client disconnected")

if __name__ == "__main__":
    print("Starting WebSocket server...")
    with serve(websocket_handler, "localhost", 8765) as server:
        print("WebSocket server started at ws://localhost:8765")
        server.serve_forever()