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
            if peak > args.thr:
                print("kontol")
                kepala.move(180)
                send_request("kontol")
            else:
                print("kasu")
                kepala.move(0)
                send_request("asu")

        except KeyboardInterrupt:
            print('Interrupted')
            closeAudio()
        