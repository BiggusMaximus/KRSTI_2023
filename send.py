import socket
import time

# IP address and port number of the ESP32
esp32_address = ('192.168.1.100', 5005)

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the ESP32
client_socket.connect(esp32_address)

# send a string and a boolean value to the ESP32
message = 'Hello, ESP32!'
value = True
data = message + ',' + str(value)
client_socket.send(data.encode())

client_socket.close()