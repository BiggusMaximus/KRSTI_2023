from adafruit_servokit import ServoKit
import pandas as pd
import time

t = 0.95
T_DELAY = 1
Servos = ServoKit(channels=16)
stabil_order = [0, 5, 1, 4, 2, 3, 7, 6, 9, 8, 10, 11, 12, 13, 14, 15]

df = pd.read_csv('./data.csv')


def moveOrder(gerakan, order,t):
    for i in order:
        Servos.servo[i].angle = df[gerakan][i]
        time.sleep(t)

def Tari(t):
    moveOrder("stabil", stabil_order, t)

Tari(T_DELAY)

