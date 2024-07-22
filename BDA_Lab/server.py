import socket

def client_connections(client_socket):
	data = client_socket.recv(1024)
	if not data:
		return
	words = data.decode().strip()
	word_count = len(words.split())
	client_socket.send(str(word_count).encode())
	client_socket.close()

def main():
    host = '127.0.0.1'
    port = 5555
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr[0]}:{addr[1]}")
            client_connections(client_socket)
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
    	server_socket.close()

if __name__ == "__main__":
    main()

