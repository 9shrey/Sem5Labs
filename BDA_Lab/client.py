import socket
def main():
    host = '127.0.0.1'
    port = 5555
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        words = input("Enter words: ")
        client_socket.send(words.encode())
        word_count = client_socket.recv(1024).decode()
        print(f"Number of words entered: {word_count}")
    finally:
        client_socket.close()
if __name__ == "__main__":
    main()
