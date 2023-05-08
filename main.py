from audio import *
from PCA9685 import *

while True:
    try:
        peak = streamAudio()
        print(peak)

    except KeyboardInterrupt:
        print('Interrupted')
        closeAudio()
        