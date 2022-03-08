from numpy import record
import sounddevice as sd
from scipy.io.wavfile import write
from platform import python_version
from subprocess import call
import os
import socket
from requests import get
from pydub import AudioSegment

def get_connectionid():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("Connect using(For Local Networks): " + s.getsockname()[0])
    s.close()

def recorder():
    fs = 44100
    seconds = 5
    try:
        os.remove("bay/output.mp3")
    except:
        pass
    while 1:
        print("recording")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write('bay/output0.wav', fs, myrecording)
        AudioSegment.from_wav("bay/output0.wav").export("bay/output.mp3", format="mp3", bitrate="64k")
        
get_connectionid()
recorder()
