import tkinter as tk
import time
from adafruit_servokit import ServoKit
import time

Servos = ServoKit(channels=16)

root = tk.Tk()
root.title("PCA9685 Servo Control")
root.rowconfigure(tuple(range(16)), weight=1)
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=2)
N_DEGREE = 10

# Define the servo names
servo_names = ["Servo 1", "Servo 2", "Servo 3", "Servo 4", "Servo 5", "Servo 6", "Servo 7", "Servo 8", "Servo 9", "Servo 10", "Servo 11", "Servo 12", "Servo 13", "Servo 14", "Servo 15", "Servo 16"]
servo_checkboxes = []
servo_labels = ["90"] * 16
servo_objects = []
degrees_entries = []


def up(i):
    global servo_labels
    if servo_checkboxes[i].get():
        servo_labels[i] = str(int(servo_labels[i]) + N_DEGREE)
        if int(servo_labels[i]) > 180:
            servo_labels[i] = "180"
        elif int(servo_labels[i]) < 0:
            servo_labels[i] = "0"
            
        degree_label = servo_objects[i][2]
        degree_label.config(text=servo_labels[i])
        Servos.servo[i].angle = int(servo_labels[i])


def down(i):
    global servo_labels
    if servo_checkboxes[i].get():
        servo_labels[i] = str(int(servo_labels[i]) - N_DEGREE)
        if int(servo_labels[i]) > 180:
            servo_labels[i] = "180"
        elif int(servo_labels[i]) < 0:
            servo_labels[i] = "0"
        degree_label = servo_objects[i][2]
        degree_label.config(text=servo_labels[i])
        Servos.servo[i].angle = int(servo_labels[i])
    
for i in range(16):
    servo_checkboxes.append(tk.BooleanVar())
    servo_checkboxes[i].set(True)

    frame = tk.Frame(root)
    frame.grid(row=i, column=0, sticky="nsew")
    
    servo_checkbox = tk.Checkbutton(frame, text="", variable=servo_checkboxes[i])
    servo_checkbox.grid(row=0, column=0, padx=10, sticky="nsew")
    
    servo_label = tk.Label(frame, text=servo_names[i])
    servo_label.grid(row=0, column=1, padx=10, sticky="nsew")
    
    up_button = tk.Button(frame, text="^", command=lambda i=i: up(i))
    up_button.grid(row=0, column=2, sticky="nsew")
    
    down_button = tk.Button(frame, text="v", command=lambda i=i: down(i))
    down_button.grid(row=0, column=3, sticky="nsew")
    
    degree_label = tk.Label(frame, text=servo_labels[i])
    degree_label.grid(row=0, column=4, sticky="nsew")
    
    servo_objects.append((servo_checkbox, servo_label, degree_label))

root.mainloop()
