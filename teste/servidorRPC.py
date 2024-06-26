from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

users = {}
messages = []

def register_user(username, password):
    if username in users:
        return False
    users[username] = password
    return True

def authenticate_user(username, password):
    return users.get(username) == password

def list_users():
    return list(users.keys())

def send_message(username, message):
    messages.append((username, message))
    return True

def get_message_history():
    return messages

def run_rpc_server():
    server = SimpleXMLRPCServer(("0.0.0.0", 8001), requestHandler=RequestHandler)  # Use 0.0.0.0 para permitir conexões de qualquer interface de rede
    server.register_introspection_functions()
    server.register_function(register_user, 'register_user')
    server.register_function(authenticate_user, 'authenticate_user')
    server.register_function(list_users, 'list_users')
    server.register_function(send_message, 'send_message')
    server.register_function(get_message_history, 'get_message_history')
    print("Servidor RPC rodando na porta 8001...")
    server.serve_forever()

if __name__ == "__main__":
    run_rpc_server()
