from adafruit_servokit import ServoKit
import time

t = 0.1
T_DELAY = 3
Servos = ServoKit(channels=16)
SERVOS_DEGREE = [0, 65, 115, 180, 180, 0, 90, 90, 70]

def gerakSalam():
    servo_angle = [60, 0, 45, 100, 175, 65, 30, 135, 110]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]
    moveOrder(servo_angle, order,t)

def gerakCuciTangan():
    servo_angle = [135, 0, 0, 130, 175, 65, 30, 135, 110]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]
    moveOrder(servo_angle, order,t)

def moveBack():
    servo_angle = [0, 65, 115, 180, 180, 0, 90, 90, 70]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]
    moveOrder(servo_angle, order[::-1],t)

def gerakMasker():
    servo_angle = [0, 180, 120, 55, 175, 85, 75, 0, 70]
    order = [4, 6, 2, 8, 3, 7, 1, 9, 5]
    moveOrder(servo_angle, order,t)

'''
def moveOrder(servo_angle, order,t, DELAY_INCREMENT=0.001):
    order = [i-1 for i in order]
    for i in order:
        Servos.servo[i].angle = servo_angle[i]
        time.sleep(t)

'''
def moveOrder(servo_angle, order,t, DELAY_INCREMENT=0.01):
    order = [i-1 for i in order]
    for i in order:
        if SERVOS_DEGREE[i] < servo_angle[i]:
            print("========jembut=======")
            print(f"SERVOS_DEGREE {SERVOS_DEGREE[i]} | servo_angle : {servo_angle[i]}")
            for j in range(SERVOS_DEGREE[i], servo_angle[i]+1, 1):
                print(f"SERVOS_DEGREE {i} | servo_angle : {servo_angle[i]} | degree : {j}")
                Servos.servo[i].angle = j
                SERVOS_DEGREE[i] = j
                time.sleep(DELAY_INCREMENT)
                
        else:
            print("==============kontol==============")
            print(f"SERVOS_DEGREE {SERVOS_DEGREE[i]} | servo_angle : {servo_angle[i]}")
            for j in range(servo_angle[i], SERVOS_DEGREE[i], -1):
                print(f"SERVOS_DEGREE [{i}] | servo_angle : {servo_angle[i]} | degree : {j}")
                Servos.servo[i].angle = j
                SERVOS_DEGREE[i] = j
                time.sleep(DELAY_INCREMENT)
                print("asu")
            
        time.sleep(t)
        
def Tari(t):
    moveBack()
    time.sleep(t)
    print("Salam")
    gerakSalam()
    time.sleep(t)
    moveBack()
    time.sleep(t)
    print("Cuci tangan")
    gerakCuciTangan()
    time.sleep(t)
    moveBack()
    gerakMasker()
    moveBack()

Tari(T_DELAY)

