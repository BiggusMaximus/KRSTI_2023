from adafruit_servokit import ServoKit
import pandas as pd
import time

t = 0.5
T_DELAY = 1
Servos = ServoKit(channels=16)

# Protokol index slave
slave_servo_index   = [8, 14, 13, 12, 0, 1, 2, 3, 0]
# Protokol index master
master_servo_index   = [i for i in range(0,9)]
# Konstanta kalibrasi 
k = [-115, -95, -20, -360, -115, -110, -125, 180, -115]
# Index master
stabil_order        = [0, 5, 1, 4, 2, 3, 7, 6, 9, 8, 10, 11, 12, 13, 14, 15]
salam_order         = [2, 3, 0, 5, 1, 4]

# Index Slave
vampire_order       = [0, 1, 2, 3, 8, 12, 13, 14, 15]

df = pd.read_csv('./data.csv')


def moveOrder(gerakan, order, t, slave=False):
    for i in order:
        if slave:
            print(f"slave : {i} => {df[gerakan][master_servo_index[i]]} | master : {master_servo_index[i]} => {df[gerakan][master_servo_index[i]] + k[master_servo_index[i]]}")
            Servos.servo[master_servo_index[i]].angle = df[gerakan][master_servo_index[i]] + k[master_servo_index[i]]
        else:
            Servos.servo[i].angle = df[gerakan][i]
        time.sleep(t)

def Tari(t):
    # for i in range(100):
    #     print(i)
    #     moveOrder("stabil", stabil_order, t)
    #     moveOrder("salam", salam_order, t)
    #     moveOrder("stabil", salam_order, t)
        
    #     time.sleep(1)
    #     print("melambai kiri")
    #     moveOrder("melambai_kiri", salam_order, t)
    #     moveOrder("salam", salam_order, t)
    #     print("melambai kanan")
        
    #     time.sleep(1)
    #     moveOrder("melambai_kanan", salam_order, t)
    #     moveOrder("salam", salam_order, t)

    #     time.sleep(1)
    #     moveOrder("vampire", salam_order, t)
    #     moveOrder("salam", salam_order, t)

    moveOrder("vampire", vampire_order, t, slave=True)


Tari(t)

