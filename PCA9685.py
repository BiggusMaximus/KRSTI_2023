import time
import board
import busio
import Adafruit_PCA9685

# Initialize I2C bus and PCA9685 module
i2c = busio.I2C(board.SCL, board.SDA)
pca = Adafruit_PCA9685.PCA9685(address=0x40)

pca.frequency = 50

def set_servo_angle(channel, angle):
    pulse_min = 150  
    pulse_max = 600  
    pulse_length = int((angle / 180) * (pulse_max - pulse_min) + pulse_min)
    pca.channels[channel].duty_cycle = pulse_length * 65536 // 4096
