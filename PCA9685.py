import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 1
time.sleep(1)
kit.continuous_servo[0].throttle = -1
time.sleep(1)
