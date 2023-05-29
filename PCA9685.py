from adafruit_servokit import ServoKit
import pandas as pd
import time

t = 0.5
T_DELAY = 1
Servos = ServoKit(channels=16)
stabil_order = [0, 5, 1, 4, 2, 3, 7, 6, 9, 8, 10, 11, 12, 13, 14, 15]
salam_order = [2, 3, 0, 5, 1, 4]

df = pd.read_csv('./data.csv')


def moveOrder(gerakan, order,t):
    for i in order:
        Servos.servo[i].angle = df[gerakan][i]
        time.sleep(t)

def Tari(t):
    for i in range(100):
        print(i)
        moveOrder("stabil", stabil_order, t)
        print("salam")
        moveOrder("salam", salam_order, t)
        moveOrder("stabil", salam_order, t)
        
        time.sleep(1)
        print("melambai kiri")
        moveOrder("melambai_kiri", salam_order, t)
        moveOrder("salam", salam_order, t)
        print("melambai kanan")
        
        time.sleep(1)
        moveOrder("melambai_kanan", salam_order, t)
        moveOrder("salam", salam_order, t)

Tari(t)

