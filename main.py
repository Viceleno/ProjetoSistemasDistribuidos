import threading
from servidorRPC import run_rpc_server
from servidorWebSocket import start_websocket_server

if __name__ == "__main__":
    # Iniciar o servidor RPC em uma thread separada
    thread_rpc = threading.Thread(target=run_rpc_server)
    thread_rpc.start()

    # Iniciar o servidor WebSocket em uma thread separada
    thread_websocket = threading.Thread(target=start_websocket_server)
    thread_websocket.start()

    # Manter a thread principal ativa
    thread_rpc.join()
    thread_websocket.join()
