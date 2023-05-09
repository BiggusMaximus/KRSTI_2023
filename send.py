import socket
import time

# Define the IP address and port of the ESP32
ESP32_IP = '192.168.1.100'
ESP32_PORT = 1234

# Create a socket and connect to the ESP32
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ESP32_IP, ESP32_PORT))
print("Socket Innit")

# Send a string and a boolean to the ESP32

def send_data(data):
    if isinstance(data, bool):
        sock.sendall(data.encode())
    if isinstance(data, str):
        sock.sendall(data.to_bytes(1, byteorder='little'))




# # Close the socket
# sock.close()