import RPi.GPIO as GPIO

ky_pin = 3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(ky_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    print(GPIO.input(ky_pin))