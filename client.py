import socket

HOST = "127.0.0.1"
PORT = 2121

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = client_socket.recv(1024).decode()
print("Server:", message)

username = input("Enter username: ")
client_socket.sendall(username.encode())

message = client_socket.recv(1024).decode()
print("Server:", message)

password = input("Enter password: ")
client_socket.sendall(password.encode())

response = client_socket.recv(1024).decode()
print("Server:", response)

client_socket.close()
