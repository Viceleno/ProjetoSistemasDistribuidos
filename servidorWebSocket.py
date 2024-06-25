import asyncio
import websockets
import xmlrpc.client
import threading

conectando_clientes = set()

async def handler(websocket, path):
    conectando_clientes.add(websocket)
    try:
        async for message in websocket:
            with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
                proxy.add_message("User", message)
                for client in conectando_clientes:
                    if client != websocket:
                        await client.send(message)
    except websockets.ConnectionClosed:
        pass
    finally:
        conectando_clientes.remove(websocket)

async def run_websocket_server():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket Server running on port 8765...")
        await asyncio.Future()  # Run forever

def start_websocket_server():
    asyncio.run(run_websocket_server())

if __name__ == "__main__":
    # Start the WebSocket server in a separate thread
    websocket_thread = threading.Thread(target=start_websocket_server)
    websocket_thread.start()

    # Keep the main thread alive
    websocket_thread.join()
