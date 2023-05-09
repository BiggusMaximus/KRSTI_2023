import socket

ESP32_IP = "192.168.18.168" # replace with the actual IP address of your ESP32
ESP32_PORT = 80

message = "ADA"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP32_IP, ESP32_PORT))

# Prepare the request string

def sendData(message):
    request = f"GET /message?message={message} HTTP/1.1\r\nHost: {ESP32_IP}\r\n\r\n"
    sock.sendall(request.encode())
    response = sock.recv(4096).decode()
    print(response)
    


