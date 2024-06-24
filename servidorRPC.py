from xmlrpc.server import SimpleXMLRPCServer
import threading

class ChatRPCServer:
    def __init__(self):
        self.messages = []

    def add_message(self, user, message):
        self.messages.append((user, message))
        return True

    def get_messages(self):
        return self.messages

def run_rpc_server():
    server = SimpleXMLRPCServer(("localhost", 8000))
    server.register_instance(ChatRPCServer())
    print("RPC Server running on port 8000...")
    server.serve_forever()

# Start the RPC server in a separate thread
rpc_thread = threading.Thread(target=run_rpc_server)
rpc_thread.start()
