# Custom FTP Server Using Socket Programming

## Project Overview

This project implements a simple **Custom FTP Server and Client** using **Python Socket Programming**. The system uses TCP sockets to establish communication between a client and a server.

The project provides basic file transfer functionality, including user authentication, listing files, uploading files from the client to the server, and downloading files from the server to the client.

This project is developed as part of a **Socket Programming Homework**.

---

## Features

The Custom FTP Server supports the following features:

* TCP socket-based client-server communication
* Username and password authentication
* List files available on the server
* Upload files from client to server
* Download files from server to client
* Quit and close the connection
* File transfer using file size-based transmission
* Support for text and binary files

---

## Technologies Used

* **Programming Language:** Python 3
* **Networking:** TCP Socket Programming
* **Libraries:**

  * `socket`
  * `os`

No external Python packages are required.

---

## Project Structure

```text
Custom-Ftp-Server-Socket/
│
├── server.py
├── client.py
├── README.md
│
├── client_files/
│   └── upload_file.txt
│
└── server_files/
    ├── sample.jpeg
    ├── sample.txt
    ├── some useful link.pdf
    └── upload_file.txt
```

### File Description

**`server.py`**
Contains the FTP server implementation. It handles client connections, authentication, file listing, file uploading, and file downloading.

**`client.py`**
Contains the FTP client implementation. It connects to the server and allows the user to perform FTP operations.

**`server_files/`**
Stores files available on the server.

**`client_files/`**
Stores files on the client side. Uploaded and downloaded files are handled through this folder.

**`README.md`**
Contains project information and instructions for running and using the system.

---

## Requirements

Make sure Python 3 is installed on your computer.

You can check the Python version using:

```bash
python --version
```

No additional packages need to be installed because the project uses Python's built-in libraries.

---

## How to Run the Project

### Step 1: Clone the Repository

Clone this repository from GitHub:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Then enter the project directory:

```bash
cd Custom-Ftp-Server-Socket
```

---

### Step 2: Start the Server

Open a terminal and run:

```bash
python server.py
```

You should see:

```text
FTP Server started on port 2121
Waiting for client connection...
```

The server is now ready to accept client connections.

---

### Step 3: Start the Client

Open another terminal in the same project directory and run:

```bash
python client.py
```

The client will connect to the FTP server.

---

## Login Information

For testing purposes, the default login credentials are:

```text
Username: admin
Password: 1234
```

The client must provide the correct username and password before accessing the FTP commands.

---

## Available Commands

After successful login, the following commands are available:

### 1. LIST

The `LIST` command displays the files stored in the server's `server_files` directory.

Example:

```text
Enter command: LIST

Files on server:
sample.jpeg
sample.txt
some useful link.pdf
```

---

### 2. UPLOAD

The `UPLOAD` command transfers a file from the client's `client_files` directory to the server's `server_files` directory.

Example:

```text
Enter command: UPLOAD
Server: Enter filename:
Enter filename: upload_file.txt

Server: READY
Server: UPLOAD_SUCCESS
```

After a successful upload, the file will appear in:

```text
server_files/
```

---

### 3. DOWNLOAD

The `DOWNLOAD` command transfers a file from the server's `server_files` directory to the client's `client_files` directory.

Example:

```text
Enter command: DOWNLOAD
Server: Enter filename:
Enter filename: sample.txt

File size: 45 bytes
DOWNLOAD_SUCCESS: sample.txt
```

After a successful download, the file will appear in:

```text
client_files/
```

---

### 4. QUIT

The `QUIT` command closes the current client-server connection.

Example:

```text
Enter command: QUIT
Server: Goodbye!
```

---

## Communication Architecture

The project follows a client-server architecture:

```text
             TCP Connection
      ┌────────────────────────┐
      │                        │
      ▼                        │
┌─────────────┐          ┌─────────────┐
│    Client   │          │    Server   │
│             │          │             │
│   Login     │─────────►│ Authentication
│   LIST      │─────────►│ File Listing
│   UPLOAD    │─────────►│ File Storage
│   DOWNLOAD  │◄─────────│ File Transfer
│   QUIT      │─────────►│ Connection
└─────────────┘          └─────────────┘
```

The client and server communicate using **TCP sockets**. TCP provides reliable and ordered delivery of data during file transfer.

---

## File Transfer Method

The project uses a **file-size-based transmission method**.

For uploading:

1. The client sends the filename.
2. The server confirms that it is ready.
3. The client sends the file size.
4. The client sends the file data in chunks.
5. The server receives the specified number of bytes.
6. The server sends an upload success message.

For downloading:

1. The client requests a filename.
2. The server checks whether the file exists.
3. The server sends the file size.
4. The client confirms that it is ready.
5. The server sends the file data in chunks.
6. The client saves the received file.

This approach allows both text and binary files to be transferred.

---

## Testing

The following operations were tested:

| Operation           | Status     |
| ------------------- | ---------- |
| TCP Connection      | Successful |
| User Authentication | Successful |
| LIST                | Successful |
| UPLOAD              | Successful |
| DOWNLOAD            | Successful |
| QUIT                | Successful |

---

## Limitations

This is an educational implementation of a custom FTP-like system and is not intended to replace the standard FTP protocol.

Current limitations include:

* Single command operation per client connection
* Basic username/password authentication
* No encryption
* No multiple simultaneous client handling
* No advanced FTP features such as directory navigation

---

## Conclusion

The project demonstrates how **TCP socket programming** can be used to build a basic client-server file transfer system.

The implemented system provides authentication and essential file management operations such as listing, uploading, and downloading files. It also demonstrates reliable file transmission between a client and server using Python sockets.

---

## Author

**Student Name:** Maria Nushrat Mahia
**Project:** Custom FTP Server Using Socket Programming
**Language:** Python
