import asyncio
import websockets

connected_users = set()

async def handler(websocket, path):
    connected_users.add(websocket)
    try:
        async for message in websocket:
            for user in connected_users:
                if user != websocket:
                    await user.send(message)
    finally:
        connected_users.remove(websocket)

async def run_websocket_server():
    print("Servidor WebSocket rodando na porta 8766...")
    async with websockets.serve(handler, "0.0.0.0", 8766):  # Use 0.0.0.0 para permitir conexões de qualquer interface de rede
        await asyncio.Future()

def start_websocket_server():
    asyncio.run(run_websocket_server())
