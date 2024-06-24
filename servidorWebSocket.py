import asyncio
import websockets
import xmlrpc.client

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
                proxy.add_message("User", message)
                for client in connected_clients:
                    if client != websocket:
                        await client.send(message)
    except websockets.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def run_websocket_server():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket Server running on port 8765...")
        await asyncio.Future()  # Run forever

# Start the WebSocket server in a separate thread
websocket_thread = threading.Thread(target=lambda: asyncio.run(run_websocket_server()))
websocket_thread.start()
