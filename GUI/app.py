import tkinter as tk
import Adafruit_PCA9685

N_SERVO = 1
class ServoPCA9685:
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(int(60))
        # Move to 90 degree first
        self.move(90)

    def move(self, pos):
        pulse = int((650-150)/180*pos+150+self.ZeroOffset)
        self.pwm.set_pwm(self.Channel, 0, pulse)

    def reset(self):
        self.move(int(90))
        print('RESET TO 90')

# Initialize the servo objects
servos = []
for i in range(N_SERVO):
    servos.append(ServoPCA9685(i, 0))

# Create the GUI
root = tk.Tk()
root.title("PCA9685 Servo Control")
root.geometry("500x500")

# Define the servo names
servo_names = ["Servo 1", "Servo 2", "Servo 3", "Servo 4", "Servo 5", "Servo 6", "Servo 7", "Servo 8", "Servo 9", "Servo 10", "Servo 11", "Servo 12", "Servo 13", "Servo 14", "Servo 15", "Servo 16"]
# Create the servo checkboxes
servo_checkboxes = []
for i in range(N_SERVO):
    servo_checkboxes.append(tk.BooleanVar(value=True))

# Create the servo labels and up/down buttons
frame = tk.Frame(root)
frame.pack(expand=True, fill="both")
for i in range(N_SERVO):
    # Servo label
    servo_label = tk.Label(frame, text=servo_names[i], width=8, anchor="w")
    servo_label.grid(row=i, column=0, padx=(5,0), pady=(5,0))

    # Servo checkbox
    servo_checkbox = tk.Checkbutton(frame, text="", variable=servo_checkboxes[i])
    servo_checkbox.grid(row=i, column=1, padx=0, pady=(5,0))

    # Servo up button
    servo_up_button = tk.Button(frame, text="↑", width=2, command=lambda i=i: servos[i].move(int(90)+5))
    servo_up_button.grid(row=i, column=2, padx=0, pady=(5,0))

    # Servo down button
    servo_down_button = tk.Button(frame, text="↓", width=2, command=lambda i=i: servos[i].move(int(90)-5))
    servo_down_button.grid(row=i, column=3, padx=0, pady=(5,0))

# Quit button
quit_button = tk.Button(root, text="Quit", command=root.quit)
quit_button.pack(side="bottom", pady=10)

root.mainloop()