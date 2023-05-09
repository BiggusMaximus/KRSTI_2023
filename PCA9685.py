import Adafruit_PCA9685
import time

class ServoPCA9685:
    def __init__(self, Channel, ZeroOffset):
        self.Channel = Channel
        self.ZeroOffset = ZeroOffset
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
        self.pwm.set_pwm_freq(int(60))
        self.current_pos = 90

    def move(self, pos, speed=1.0):
        current_pos = self.current_pos
        step = 1 if pos > current_pos else -1
        delay = 0.01 / speed
        for i in range(current_pos, pos, step):
            pulse = int((650 - 150) / 180 * i + 150 + self.ZeroOffset)
            self.pwm.set_pwm(self.Channel, 0, pulse)
            self.current_pos = i  # Update current position
            time.sleep(delay)

    def reset(self):
        self.move(int(90))
        print('RESET TO 90')

def innitServo():
    # global pergelangan_tangan_kanan, siku_tangan_kanan, pundakEngsel_tangan_kanan, pundakPutar_tangan_kanan, pergelangan_tangan_kiri, siku_tangan_kiri, pundakEngsel_tangan_kiri, pundakPutar_tangan_kiri, kepala
    global kepala
    # # Kanan
    # pergelangan_tangan_kanan    = ServoPCA9685(0, 0)
    # siku_tangan_kanan           = ServoPCA9685(1, 0)
    # pundakEngsel_tangan_kanan   = ServoPCA9685(2, 0)
    # pundakPutar_tangan_kanan    = ServoPCA9685(3, 0)
    
    # # Kiri
    # pergelangan_tangan_kiri     = ServoPCA9685(5, 0)
    # siku_tangan_kiri            = ServoPCA9685(6, 0)
    # pundakEngsel_tangan_kiri    = ServoPCA9685(7, 0)
    # pundakPutar_tangan_kiri     = ServoPCA9685(8, 0)

    kepala                        = ServoPCA9685(0, 0)
    print("Servo innit")

def reset():
    for i in [pergelangan_tangan_kanan, siku_tangan_kanan, pundakEngsel_tangan_kanan, pundakPutar_tangan_kanan, pergelangan_tangan_kiri, siku_tangan_kiri, pundakEngsel_tangan_kiri, pundakPutar_tangan_kiri, kepala]:
        i.reset()

innitServo()
