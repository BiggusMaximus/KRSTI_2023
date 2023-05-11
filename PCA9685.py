import time
from adafruit_servokit import ServoKit

Servos = ServoKit(channels=16)

while True:
	Servos.servo[0].angle = 180

	Servos.servo[0].angle = 90

