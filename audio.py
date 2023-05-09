import pyaudio
import numpy as np

CHUNK = 2**11
RATE = 44100
IS_MUSIC_ON = True

p=pyaudio.PyAudio()
stream=p.open(
    format=pyaudio.paInt16,
    channels=1,rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
    )

def streamAudio():
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    return int(peak)

def closeAudio():
    stream.stop_stream()
    stream.close()
    p.terminate()
