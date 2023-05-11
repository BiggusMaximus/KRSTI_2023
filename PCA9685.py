import time
from adafruit_servokit import ServoKit

Servos = ServoKit(channels=16)

Servos.servo[0].angle = 180
time.sleep(1)
Servos.servo[0].angle = -180
time.sleep(1)
