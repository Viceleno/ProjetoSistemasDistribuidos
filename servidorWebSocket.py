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
        await asyncio.Future()  

def start_websocket_server():
    asyncio.run(run_websocket_server())

if __name__ == "__main__":
    # Começan o servidor websocket em uma thread separada
    websocket_thread = threading.Thread(target=start_websocket_server)
    websocket_thread.start()

    # Mantenha a thread main aberta
    websocket_thread.join()
