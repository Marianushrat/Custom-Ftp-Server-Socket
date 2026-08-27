import socket
import os

HOST = "127.0.0.1"
PORT = 2121

CLIENT_FOLDER = "client_files"

os.makedirs(CLIENT_FOLDER, exist_ok=True)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

# ---------------- WELCOME ----------------

message = client_socket.recv(1024).decode()
print("Server:", message)

# ---------------- USERNAME ----------------

message = client_socket.recv(1024).decode()
print("Server:", message)

username = input("Enter username: ")
client_socket.sendall(username.encode())

# ---------------- PASSWORD ----------------

message = client_socket.recv(1024).decode()
print("Server:", message)

password = input("Enter password: ")
client_socket.sendall(password.encode())

# ---------------- LOGIN RESULT ----------------

response = client_socket.recv(1024).decode()
print("Server:", response)

if "LOGIN_SUCCESS" in response:

    # ---------------- COMMAND ----------------

    message = client_socket.recv(1024).decode()
    print("Server:", message)

    command = input("Enter command: ").strip().upper()
    client_socket.sendall(command.encode())

    # ---------------- LIST ----------------

    if command == "LIST":

        response = client_socket.recv(4096).decode()
        print(response)

    # ---------------- UPLOAD ----------------

    elif command == "UPLOAD":

        message = client_socket.recv(1024).decode()
        print("Server:", message)

        filename = input("Enter filename: ").strip()

        filepath = os.path.join(CLIENT_FOLDER, filename)

        if not os.path.exists(filepath):

            print("File not found:", filepath)

        else:

            client_socket.sendall(filename.encode())

            response = client_socket.recv(1024).decode()
            print("Server:", response)

            if "READY" in response:

                file_size = os.path.getsize(filepath)

                # Send file size
                client_socket.sendall(
                    str(file_size).encode()
                )

                # Send file data
                with open(filepath, "rb") as file:

                    while True:

                        data = file.read(4096)

                        if not data:
                            break

                        client_socket.sendall(data)

                response = client_socket.recv(1024).decode()
                print("Server:", response)

    # ---------------- DOWNLOAD ----------------

    elif command == "DOWNLOAD":

        message = client_socket.recv(1024).decode()
        print("Server:", message)

        filename = input("Enter filename: ").strip()

        # Send filename
        client_socket.sendall(filename.encode())

        response = client_socket.recv(1024).decode()

        # File not found
        if response == "FILE_NOT_FOUND":

            print("Server: File not found.")

        # File found
        elif response.startswith("FILE_SIZE:"):

            file_size = int(
                response.split(":")[1]
            )

            print(f"File size: {file_size} bytes")

            # Tell server we are ready
            client_socket.sendall(b"READY")

            filepath = os.path.join(
                CLIENT_FOLDER,
                filename
            )

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

                print(
                    f"DOWNLOAD_SUCCESS: {filename}"
                )

            else:

                print("DOWNLOAD_FAILED")

    # ---------------- QUIT ----------------

    elif command == "QUIT":

        response = client_socket.recv(1024).decode()
        print("Server:", response)

    # ---------------- INVALID COMMAND ----------------

    else:

        response = client_socket.recv(1024).decode()
        print("Server:", response)

else:

    print("Access denied. Invalid username or password.")


client_socket.close()
