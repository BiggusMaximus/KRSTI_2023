import socket
import time


esp32_address = ('192.168.18.168', 5005)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(esp32_address)


