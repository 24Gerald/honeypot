import socket
import threading

def handle_client(client_socket):
    client_socket.send(b"Fake SSH Server. Enter Password: ")
    response = client_socket.recv(1024)
    print(f"[*] Attack attempt from {client_socket.getpeername()} with password: {response.decode().strip()}")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 2222))  # Fake SSH Port
server.listen(5)
print("[*] Honeypot listening on port 2222")

while True:
    client, addr = server.accept()
    print(f"[*] Connection from {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
