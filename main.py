from audio import *
from PCA9685 import *
from send import *
import argparse

parser = argparse.ArgumentParser()  
parser.add_argument("--thr", help='Masukin limit threshold dari suara (0-1023) : ', default=500, type = int)  


if __name__ == '__main__':
    args = parser.parse_args()  
    print(args.thr)
    print(kepala)

    while True:
        try:
            peak = streamAudio()
            if peak > 500:
                print("kontol")
                kepala.move(180)
                client_socket.send('Hello, ESP32!'.encode())
            else:
                print("kasu")
                kepala.move(0)
                client_socket.send('Hello, ESP32!'.encode())
            
        except KeyboardInterrupt:
            print('Interrupted')
            closeAudio()
        