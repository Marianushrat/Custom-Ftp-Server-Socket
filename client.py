import socket

HOST = "127.0.0.1"
PORT = 2121

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

message = client_socket.recv(1024).decode()

print("Server:", message)

client_socket.close()
