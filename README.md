# 🚀 Custom FTP Server Using Socket Programming

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&duration=3000&pause=1000&color=36BCF7&center=true&vCenter=true&width=800&lines=Custom+FTP+Server;Socket+Programming+with+Python;TCP+Client-Server+File+Transfer;Upload+%7C+Download+%7C+List" alt="Typing Animation" />

</p>

<p align="center">
  <b>A simple, custom FTP-like file transfer system built with Python TCP sockets.</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)
![Socket](https://img.shields.io/badge/Networking-TCP%20Sockets-orange)
![Protocol](https://img.shields.io/badge/Protocol-Custom%20FTP-purple)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

## 🌐 Project Overview

**Custom FTP Server Using Socket Programming** is a lightweight client-server file transfer system developed using **Python TCP socket programming**.

The project demonstrates how a reliable file transfer application can be built from the ground up without using external FTP libraries.

The system provides basic FTP-like operations such as:

* 🔐 User authentication
* 📂 File listing
* ⬆️ File upload
* ⬇️ File download
* 🚪 Connection termination

The main goal of this project is to understand **TCP socket communication, client-server architecture, authentication, and reliable file transmission**.

---

## ✨ Features

| Feature               | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| 🔌 TCP Connection     | Establishes reliable communication between client and server |
| 🔐 Authentication     | Username and password based login                            |
| 📋 LIST               | Displays files available on the server                       |
| ⬆️ UPLOAD             | Transfers files from client to server                        |
| ⬇️ DOWNLOAD           | Transfers files from server to client                        |
| 🚪 QUIT               | Closes the client-server connection                          |
| 📦 Binary Transfer    | Supports text and binary files                               |
| 📏 File Size Protocol | Uses file size to control reliable file transmission         |

---

## 🛠️ Technologies Used

### Programming Language

🐍 **Python 3**

### Networking

🌐 **TCP Socket Programming**

### Built-in Libraries

```text
socket
os
```

No external Python packages are required.

---

## 🏗️ System Architecture

```text
                     TCP CONNECTION
                           │
                           ▼
              ┌────────────────────────┐
              │      CUSTOM FTP        │
              │         SYSTEM         │
              └────────────────────────┘
                    ▲             ▲
                    │             │
             Commands          File Data
                    │             │
                    │             │
          ┌─────────┴───┐     ┌───┴─────────┐
          │             │     │             │
          │   CLIENT    │◄───►│   SERVER    │
          │             │     │             │
          └─────────────┘     └─────────────┘
                 │                   │
                 ▼                   ▼
          client_files/       server_files/
```

---

## 🔄 How It Works

The communication follows a simple sequence:

```text
        ┌───────────────┐
        │ Start Server  │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ Start Client  │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ TCP Connect   │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ Authentication│
        └───────┬───────┘
                │
                ▼
        ┌─────────────────────┐
        │ Select FTP Command  │
        └───────┬─────────────┘
                │
        ┌───────┼───────────────┐
        ▼       ▼       ▼       ▼
      LIST    UPLOAD DOWNLOAD  QUIT
        │       │       │       │
        ▼       ▼       ▼       ▼
      Files   Client   Server  Close
              →Server  →Client
```

---

## 📁 Project Structure

```text
Custom-Ftp-Server-Socket/
│
├── 📄 server.py
├── 📄 client.py
├── 📄 README.md
│
├── 📂 client_files/
│   └── upload_file.txt
│
└── 📂 server_files/
    ├── sample.jpeg
    ├── sample.txt
    ├── some useful link.pdf
    └── upload_file.txt
```

### `server.py`

Responsible for:

* Creating the TCP server
* Accepting client connections
* Authentication
* Processing commands
* Listing server files
* Receiving uploaded files
* Sending downloaded files

### `client.py`

Responsible for:

* Connecting to the server
* Sending login credentials
* Sending FTP commands
* Uploading files
* Downloading files
* Displaying server responses

### `client_files/`

Stores files available on the client side.

### `server_files/`

Stores files available on the server side.

---

## ⚙️ Requirements

Before running the project, make sure **Python 3** is installed.

Check your Python version:

```bash
python --version
```

Example:

```text
Python 3.12.x
```

No additional packages are required.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Marianushrat/Custom-Ftp-Server-Socket.git
```

Move into the project directory:

```bash
cd Custom-Ftp-Server-Socket
```

---

### 2. Start the Server

Open a terminal and run:

```bash
python server.py
```

Expected output:

```text
FTP Server started on port 2121
Waiting for client connection...
```

---

### 3. Start the Client

Open another terminal in the project directory:

```bash
python client.py
```

The client will connect to the server.

---

## 🔐 Login Credentials

For testing purposes, the project currently uses:

```text
Username: admin
Password: 1234
```

After successful authentication, the client can access the available commands.

---

# 💻 Available Commands

## 📋 1. LIST

Displays all files stored inside the server's `server_files` directory.

Example:

```text
Enter command: LIST

Files on server:
sample.jpeg
sample.txt
some useful link.pdf
```

---

## ⬆️ 2. UPLOAD

Uploads a file from:

```text
client_files/
```

to:

```text
server_files/
```

Example:

```text
Enter command: UPLOAD

Server: Enter filename:
Enter filename: upload_file.txt

Server: READY
Server: UPLOAD_SUCCESS
```

After successful upload:

```text
client_files/
      │
      │
      ▼
server_files/
```

---

## ⬇️ 3. DOWNLOAD

Downloads a file from:

```text
server_files/
```

to:

```text
client_files/
```

Example:

```text
Enter command: DOWNLOAD

Server: Enter filename:
Enter filename: sample.txt

File size: 45 bytes
DOWNLOAD_SUCCESS: sample.txt
```

The downloaded file will be saved inside:

```text
client_files/
```

---

## 🚪 4. QUIT

Closes the current connection.

Example:

```text
Enter command: QUIT

Server: Goodbye!
```

---

# 📦 File Transfer Protocol

This project uses a **file-size-based transmission method** instead of relying on a special end-of-file marker.

### Upload Process

```text
Client                         Server
  │                              │
  │──── UPLOAD ────────────────►│
  │──── Filename ──────────────►│
  │◄──── READY ─────────────────│
  │──── File Size ─────────────►│
  │──── File Data ─────────────►│
  │◄──── UPLOAD_SUCCESS ────────│
  │                              │
```

### Download Process

```text
Client                         Server
  │                              │
  │──── DOWNLOAD ──────────────►│
  │──── Filename ──────────────►│
  │◄──── File Size ─────────────│
  │──── READY ─────────────────►│
  │◄──── File Data ─────────────│
  │                              │
  │   File saved locally         │
```

Using the file size allows the receiver to determine exactly how many bytes should be received.

---

# 🧪 Testing

The following operations were tested during development:

| Test                    | Result |
| ----------------------- | :----: |
| TCP connection          |    ✅   |
| Username authentication |    ✅   |
| Password authentication |    ✅   |
| LIST command            |    ✅   |
| UPLOAD command          |    ✅   |
| DOWNLOAD command        |    ✅   |
| QUIT command            |    ✅   |
| Text file transfer      |    ✅   |
| Binary file transfer    |    ✅   |

---

# 🎯 Learning Objectives

This project demonstrates practical concepts of:

* TCP socket creation
* Client-server communication
* IP address and port binding
* TCP connection establishment
* Authentication
* Network data transmission
* File handling
* Binary file transfer
* Client-server protocol design
* Reliable data transfer using file size

---

# ⚠️ Limitations

This project is designed for **educational purposes** and is not intended to replace the standard FTP protocol.

Current limitations include:

* Basic username/password authentication
* No encryption
* No TLS/SSL
* One main command per client connection
* No advanced FTP directory navigation
* No multi-user account management
* No anonymous login
* No production-level security

---

# 🔮 Future Improvements

Possible future enhancements include:

* 👥 Multiple simultaneous clients using threading
* 🔒 Encrypted communication using TLS
* 👤 Multiple user accounts
* 📁 Directory navigation
* 🗑️ File deletion
* 🔄 Persistent client sessions
* 📊 Transfer progress indicator
* 📝 Server logging system
* 🛡️ Improved authentication and authorization

---

# 👩‍💻 Author

<p align="center">

### Maria Nushrat Mahia

**Socket Programming Homework Project**

</p>

<p align="center">

<a href="https://github.com/Marianushrat">
<img src="https://img.shields.io/badge/GitHub-Maria%20Nushrat%20Mahia-black?logo=github" alt="GitHub"/>
</a>

</p>

---

# 📌 Repository

🔗 **GitHub Repository**

https://github.com/Marianushrat/Custom-Ftp-Server-Socket

---

## ⭐ Project Summary

> A custom FTP-like file transfer system developed with Python TCP Socket Programming, supporting authentication, file listing, upload, download, and connection management.

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3500&pause=800&color=8B5CF6&center=true&vCenter=true&width=700&lines=Built+with+Python+%F0%9F%90%8D;Powered+by+TCP+Sockets+%F0%9F%8C%90;Client+%E2%86%94+Server+File+Transfer+%F0%9F%93%A1;Thanks+for+visiting!+%E2%9C%A8" alt="Animated Footer" />

</p>
