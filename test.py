from audio import *
from send import *
import argparse

parser = argparse.ArgumentParser()  
parser.add_argument("--thr", help='Masukin limit threshold dari suara (0-1023) : ', default=500, type = int)  


if __name__ == '__main__':
    args = parser.parse_args()  
    print(args.thr)

    while True:
        try:
            peak = streamAudio()
            if peak > 500:
                print("kontol")
                client_socket.send('Hello, ESP32!'.encode())
            else:
                print("kasu")
                client_socket.send('Hello, ESP32!'.encode())
            
        except KeyboardInterrupt:
            print('Interrupted')
            closeAudio()
        