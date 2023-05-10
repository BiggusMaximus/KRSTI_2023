Copy code
import tkinter as tk
import Adafruit_PCA9685

class ServoPCA9685:
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(int(60))
        self.position = tk.IntVar()
        self.move(90)

    def move(self, pos):
        pulse = int((650-150)/180*pos+150+self.ZeroOffset)
        self.pwm.set_pwm(self.Channel, 0, pulse)
        self.position.set(pos)

    def reset(self):
        self.move(90)
        print('RESET TO 90')

root = tk.Tk()
root.title("PCA9685 Servo Control")
root.geometry('800x480')

# Define the servo names
servo_names = ["Servo 1", "Servo 2", "Servo 3", "Servo 4", "Servo 5", "Servo 6", "Servo 7", "Servo 8", "Servo 9", "Servo 10", "Servo 11", "Servo 12", "Servo 13", "Servo 14", "Servo 15", "Servo 16"]

# Create the servo checkboxes and labels
servo_checkboxes = []
servo_labels = []
servo_objects = []
degrees_entries = []

for i in range(16):
    servo_checkboxes.append(tk.BooleanVar())
    servo_checkboxes[i].set(True)

    frame = tk.Frame(root)
    frame.grid(row=i, column=0, sticky="w")
    
    servo_checkbox = tk.Checkbutton(frame, text="", variable=servo_checkboxes[i])
    servo_checkbox.grid(row=0, column=0, padx=10)
    
    servo_label = tk.Label(frame, text=servo_names[i])
    servo_label.grid(row=0, column=1, padx=10)
    
    servo = ServoPCA9685(i, 0)
    servo_objects.append(servo)
    
    up_button = tk.Button(frame, text="^", command=lambda x=i: servo.move(servo.position.get()+1))
    up_button.grid(row=0, column=2)
    
    down_button = tk.Button(frame, text="v", command=lambda x=i: servo.move(servo.position.get()-1))
    down_button.grid(row=0, column=3)
    
    degree_label = tk.Label(frame, textvariable=servo.position)
    degree_label.grid(row=0, column=4)

    degrees_entries.append(tk.Entry(frame, width=10))
    degrees_entries[i].grid(row=0, column=5)
    degrees_entries[i].insert(0, "90")

# Create the reset button
reset_button = tk.Button(root, text="Reset All", command=lambda: [servo.reset() for servo in servo_objects])
reset_button.grid(row=16, column=0, pady=20)

root.mainloop()