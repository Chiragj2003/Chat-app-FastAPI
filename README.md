# FastAPI WebSocket Chat Application

This is a simple chat application built using FastAPI and WebSockets. The application allows real-time communication between multiple clients connected to the server.

## Features

- Real-time messaging using WebSockets.
- Broadcast messages to all connected clients.
- Simple HTML frontend to send and receive messages.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-chat-app.git
    cd fastapi-chat-app
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install fastapi uvicorn
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your web browser and go to `http://localhost:8000`. You should see a simple chat interface.

3. Open multiple browser tabs or windows to test real-time communication between clients.

## Code Explanation

### HTML and JavaScript

The HTML file creates a simple chat interface with an input field, a send button, and a message list. JavaScript handles the WebSocket connection, sending messages to the server, and receiving and displaying messages from the server.

### FastAPI

#### ConnectionManager Class

The `ConnectionManager` class manages WebSocket connections:

- `connect`: Adds a WebSocket connection to the list of active connections.
- `disconnect`: Removes a WebSocket connection from the list of active connections.
- `send_personal_message`: Sends a message to a specific WebSocket connection.
- `broadcast`: Sends a message to all active WebSocket connections.

#### Endpoints

- `@app.get("/")`: Serves the HTML page.
- `@app.websocket("/ws")`: Handles WebSocket connections. When a client connects, it is added to the connection manager. Messages received from a client are broadcast to all connected clients. If a client disconnects, it is removed from the connection manager, and a disconnect message is broadcast to all connected clients.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
