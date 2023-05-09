import socket
import time

ESP32_IP = "192.168.18.168"
ESP32_PORT = 80

def send_request(message):
    time.seep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ESP32_IP, ESP32_PORT))
        request = f"GET /message?message={message} HTTP/1.1\r\nHost: {ESP32_IP}\r\n\r\n"
        sock.sendall(request.encode())
        response = sock.recv(4096).decode()
        print(response)

