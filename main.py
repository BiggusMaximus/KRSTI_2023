from audio import *
from PCA9685 import *


if __name__ == '__main__':
    set_servo_angle(7, 90)
    while True:
        try:
            peak = streamAudio()
            print(peak)

        except KeyboardInterrupt:
            print('Interrupted')
            closeAudio()
        