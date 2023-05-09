from audio import *
# from PCA9685 import *
import time
import board
import busio
import Adafruit_PCA9685
from adafruit_servokit import ServoKit

# Initialize I2C bus and PCA9685 module
i2c = busio.I2C(board.SCL, board.SDA)
pca = Adafruit_PCA9685.PCA9685(address=0x40)

servo = ServoKit(channels=16)

pca.frequency = 50

def set_servo_angle(channel, angle):
    pulse_min = 150  
    pulse_max = 600  
    pulse_length = int((angle / 180) * (pulse_max - pulse_min) + pulse_min)
    pca.channels[channel].duty_cycle = pulse_length * 65536 // 4096


if __name__ == '__main__':
    servo.servo[7].angle = 180
    while True:
        try:
            peak = streamAudio()
            print(peak)

        except KeyboardInterrupt:
            print('Interrupted')
            closeAudio()
        