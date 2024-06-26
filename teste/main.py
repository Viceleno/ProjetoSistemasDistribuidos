import threading
from servidorRPC import run_rpc_server
from servidorWebSocket import start_websocket_server

if __name__ == "__main__":
    # Iniciar o servidor RPC em uma thread separada
    rpc_thread = threading.Thread(target=run_rpc_server)
    rpc_thread.start()

    # Iniciar o servidor WebSocket em uma thread separada
    websocket_thread = threading.Thread(target=start_websocket_server)
    websocket_thread.start()

    # Manter a thread principal ativa
    rpc_thread.join()
    websocket_thread.join()
