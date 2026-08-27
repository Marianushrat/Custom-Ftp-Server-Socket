import socket

HOST = "0.0.0.0"
PORT = 2121

USERNAME = "admin"
PASSWORD = "1234"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"FTP Server started on port {PORT}")
print("Waiting for client connection...")

while True:
    client_socket, client_address = server_socket.accept()

    print(f"Client connected: {client_address}")

    client_socket.sendall(b"Welcome to Custom FTP Server!\n")

    client_socket.sendall(b"Username: ")
    username = client_socket.recv(1024).decode().strip()

    client_socket.sendall(b"Password: ")
    password = client_socket.recv(1024).decode().strip()

    if username == USERNAME and password == PASSWORD:
        client_socket.sendall(b"LOGIN_SUCCESS\n")
        print(f"User '{username}' logged in successfully.")
    else:
        client_socket.sendall(b"LOGIN_FAILED\n")
        print(f"Login failed for user '{username}'.")

    client_socket.close()
