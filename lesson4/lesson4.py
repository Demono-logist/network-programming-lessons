import socket
import threading

# Task 1: Echo Server and Client
# Easy: Echo Server
def echo_server():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Echo server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

# Easy: Echo Client
def echo_client():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = "Hello, Echo Server!"
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

# Task 2: Multi-Client Support
# Medium: Persistent Echo Server
def persistent_echo_server():
    host = '127.0.0.1'
    port = 65432

    def handle_client(conn, addr):
        print(f"Connected by {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Persistent echo server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

# Task 3: File Transfer
# Medium/Hard: File Receiving Server
def file_server():
    host = '127.0.0.1'
    port = 65433

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"File server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            with open('received_file.txt', 'wb') as file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)

# Medium: File Sending Client
def file_client():
    host = '127.0.0.1'
    port = 65433

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        with open('file_to_send.txt', 'rb') as file:
            while (chunk := file.read(1024)):
                client_socket.sendall(chunk)

if __name__ == "__main__":

    # echo_server()
    # echo_client()
    # persistent_echo_server()
    # file_server()
    # file_client()
    pass
