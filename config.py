import pyaudio

class Config:
    OUTPUT_FILENAME = "recording.wav"
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
