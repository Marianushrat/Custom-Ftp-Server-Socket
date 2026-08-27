import socket
import os

HOST = "0.0.0.0"
PORT = 2121

USERNAME = "admin"
PASSWORD = "1234"

SERVER_FOLDER = "server_files"

os.makedirs(SERVER_FOLDER, exist_ok=True)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"FTP Server started on port {PORT}")
print("Waiting for client connection...")

while True:
    client_socket, client_address = server_socket.accept()

    print(f"Client connected: {client_address}")

    client_socket.sendall(b"Welcome to Custom FTP Server!\n")

    # ---------------- LOGIN ----------------

    client_socket.sendall(b"Username: ")
    username = client_socket.recv(1024).decode().strip()

    client_socket.sendall(b"Password: ")
    password = client_socket.recv(1024).decode().strip()

    if username == USERNAME and password == PASSWORD:

        client_socket.sendall(b"LOGIN_SUCCESS\n")
        print(f"User '{username}' logged in successfully.")

        client_socket.sendall(
            b"Enter command (LIST / UPLOAD / DOWNLOAD / QUIT): "
        )

        command = client_socket.recv(1024).decode().strip().upper()

        # ---------------- LIST ----------------

        if command == "LIST":

            files = os.listdir(SERVER_FOLDER)

            if files:
                response = "Files on server:\n"
                response += "\n".join(files)
            else:
                response = "Server folder is empty."

            client_socket.sendall(response.encode())

        # ---------------- UPLOAD ----------------

        elif command == "UPLOAD":

            client_socket.sendall(b"Enter filename: ")

            filename = client_socket.recv(1024).decode().strip()

            filepath = os.path.join(SERVER_FOLDER, filename)

            client_socket.sendall(b"READY\n")

            # Receive file size
            file_size_data = client_socket.recv(1024).decode().strip()
            file_size = int(file_size_data)

            # Receive file data
            received = 0

            with open(filepath, "wb") as file:

                while received < file_size:

                    data = client_socket.recv(
                        min(4096, file_size - received)
                    )

                    if not data:
                        break

                    file.write(data)
                    received += len(data)

            if received == file_size:

                client_socket.sendall(b"UPLOAD_SUCCESS\n")
                print(f"File uploaded successfully: {filename}")

            else:

                client_socket.sendall(b"UPLOAD_FAILED\n")
                print(f"File upload failed: {filename}")

        # ---------------- DOWNLOAD ----------------

        elif command == "DOWNLOAD":

            client_socket.sendall(b"Enter filename: ")

            filename = client_socket.recv(1024).decode().strip()

            filepath = os.path.join(SERVER_FOLDER, filename)

            if not os.path.isfile(filepath):

                client_socket.sendall(b"FILE_NOT_FOUND\n")
                print(f"File not found: {filename}")

            else:

                file_size = os.path.getsize(filepath)

                # Send file size
                client_socket.sendall(
                    f"FILE_SIZE:{file_size}".encode()
                )

                # Wait for client confirmation
                response = client_socket.recv(1024).decode().strip()

                if response == "READY":

                    with open(filepath, "rb") as file:

                        while True:

                            data = file.read(4096)

                            if not data:
                                break

                            client_socket.sendall(data)

                    print(f"File downloaded: {filename}")

        # ---------------- QUIT ----------------

        elif command == "QUIT":

            client_socket.sendall(b"Goodbye!\n")

        # ---------------- INVALID COMMAND ----------------

        else:

            client_socket.sendall(b"Invalid command.\n")

    # ---------------- LOGIN FAILED ----------------

    else:

        client_socket.sendall(b"LOGIN_FAILED\n")
        print(f"Login failed for user '{username}'.")

    client_socket.close()
