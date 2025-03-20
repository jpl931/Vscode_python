import socket
import threading

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(5)
    print(f"Server started on port {port}. Waiting for messages...")
    while True:
        client_socket, addr = server_socket.accept()
        data = client_socket.recv(1024).decode()
        print(f"\nMessage from {addr[0]}: {data}")
        client_socket.close()

def send_message(target_ip, port, message):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, port))
        client_socket.send(message.encode())
        client_socket.close()
        print("Message sent successfully.")
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    port = 12345
    local_ip = get_local_ip()
    print(f"Your local IP is: {local_ip}")
    print("Enter target IP and message to send. Press Ctrl+C to exit.")

    server_thread = threading.Thread(target=start_server, args=(port,))
    server_thread.daemon = True
    server_thread.start()

    try:
        while True:
            target_ip = input("Enter target IP: ")
            message = input("Enter message: ")
            send_message(target_ip, port, message)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()