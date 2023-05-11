from adafruit_servokit import ServoKit
import time

Servos = ServoKit(channels=16)

def gerakSalam():
    servo_angle = [60, 0, 45, 100, 175, 65, 30, 135, 110]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]
    
    for i in order:        
        Servos.servo[i-1].angle = servo_angle[i]

def gerakCuciTangan():
    servo_angle = [135, 0, 0, 130, 175, 65, 30, 135, 110]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]

    for i in order:
        Servos.servo[i-1].angle = servo_angle[i]

def moveReset():
    servo_angle = [0, 65, 115, 180, 180, 0, 90, 90, 70]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]

    for i in order:
        Servos.servo[i-1].angle = servo_angle[i]

def gerakMasker():
    servo_angle = [0, 180, 120, 55, 175, 85, 75, 0, 70]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]

    for i in order:
        Servos.servo[i-1].angle = servo_angle[i]

moveReset()
time.sleep(1)
gerakSalam()
time.sleep(1)
moveReset()
time.sleep(1)
gerakCuciTangan()
time.sleep(1)
moveReset()
time.sleep(1)
gerakMasker()
moveReset()
