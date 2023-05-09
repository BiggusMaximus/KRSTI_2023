import tkinter as tk
import board
import busio
import adafruit_pca9685
from adafruit_servokit import ServoKit

# Initialize the PCA9685 board
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels=16)
N_SERVO = 1


# Define the servo names
servo_names = ["Servo 1", "Servo 2", "Servo 3", "Servo 4", "Servo 5", "Servo 6", "Servo 7", "Servo 8", "Servo 9", "Servo 10", "Servo 11", "Servo 12", "Servo 13", "Servo 14", "Servo 15", "Servo 16"]

# Initialize the list of checkboxes to keep track of which servos are selected
servo_checkboxes = []

# Define the functions to move the servos up and down
def move_servo_up(servo_index):
    if servo_checkboxes[servo_index].get() == 1:
        current_value = int(kit.servo[servo_index].angle)
        if current_value < 180:
            kit.servo[servo_index].angle = current_value + 1

def move_servo_down(servo_index):
    if servo_checkboxes[servo_index].get() == 1:
        current_value = int(kit.servo[servo_index].angle)
        if current_value > 0:
            kit.servo[servo_index].angle = current_value - 1

# Create the main window
root = tk.Tk()
root.title("PCA9685 Servo Control")

# Define the frame to contain the servo labels, entry boxes, and checkboxes
frame = tk.Frame(root, bd=2, relief="ridge")
frame.pack(side="left", fill="both", expand=True)

# Create the servo labels and checkboxes
for i in range(N_SERVO):
    servo_label = tk.Label(frame, text=servo_names[i])
    servo_label.pack(side="top", fill="x", padx=5, pady=5)

    servo_checkbox = tk.Checkbutton(frame, text="", variable=servo_checkboxes[i])
    servo_checkbox.pack(side="left", padx=5, pady=5)
    servo_checkboxes.append(servo_checkbox)

# Create the up and down buttons for each servo
button_frame = tk.Frame(root, bd=2, relief="ridge")
button_frame.pack(side="right", fill="y")

for i in range(N_SERVO):
    up_button = tk.Button(button_frame, text="↑", command=lambda index=i: move_servo_up(index))
    up_button.pack(side="top", fill="x", padx=5, pady=5)

    down_button = tk.Button(button_frame, text="↓", command=lambda index=i: move_servo_down(index))
    down_button.pack(side="top", fill="x", padx=5, pady=5)

# Start the main loop
root.mainloop()