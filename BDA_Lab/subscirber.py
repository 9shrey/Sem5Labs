import socket

def main():
    host = '127.0.0.1'
    port = 55543
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        data = client_socket.recv(1024).decode()
        print(f"Message from server: {data}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
