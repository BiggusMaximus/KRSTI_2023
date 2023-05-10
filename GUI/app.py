import tkinter as tk
import Adafruit_PCA9685
import time

class ServoPCA9685:
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(int(60))

    def move(self, pos):
        pulse = int((650-150)/180*pos+150+self.ZeroOffset)
        self.pwm.set_pwm(self.Channel, 0, pulse)

    def reset(self):
        self.move(int(90))
        print('RESET TO 90')

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

# Define the servo names
servo_names = ["Servo 1", "Servo 2", "Servo 3", "Servo 4", "Servo 5", "Servo 6", "Servo 7", "Servo 8", "Servo 9", "Servo 10", "Servo 11", "Servo 12", "Servo 13", "Servo 14", "Servo 15", "Servo 16"]
servos = []
servo_checkboxes = []
servo_labels = ["90"] * 16
servo_objects = []
degrees_entries = []


def up(i):
    global servo_labels
    if servo_checkboxes[i].get():
        servo_labels[i] = str(int(servo_labels[i]) + 1)
        degree_label = servo_objects[i][2]
        degree_label.config(text=servo_labels[i])
        servos[i].move(int(servo_objects[i][2]))


def down(i):
    global servo_labels
    if servo_checkboxes[i].get():
        servo_labels[i] = str(int(servo_labels[i]) - 1)
        degree_label = servo_objects[i][2]
        degree_label.config(text=servo_labels[i])
        servos[i].move(int(servo_objects[i][2]))
    
for i in range(16):
    servo = ServoPCA9685(i, 0)
    servos.append(servo)
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
