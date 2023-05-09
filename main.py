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
            print(peak)
            
            # Kalo gak ada suara
            if peak < args.thr:
                IS_MUSIC_ON = False
                kepala.move(180)
                
            # Kalo ada suara
            else:
                if not IS_MUSIC_ON:
                    print("send data")
                    send_request("tempik")
                    IS_MUSIC_ON = True
                    
                kepala.move(0)


        except KeyboardInterrupt:
            print('Interrupted')
            closeAudio()
        
