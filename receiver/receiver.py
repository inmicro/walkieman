from numpy import true_divide
import sounddevice as sd
import soundfile as sf
import wget
import os
from multiprocessing import Process
import PySimpleGUI as sg

termination_status = False
def receive_call(ip):
    try:
        os.remove("output0.wav")
    except:
        pass
    url0 = f'http://{ip}:8000/output0.wav'
    print(url0)
    while 1:
        try:
            filename = wget.download(url0)
        except:
            continue
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        status = sd.wait()
    
        os.remove("output0.wav")

def main():
    layout = [
        [sg.Text("This is the receiver interface")], 
        [sg.Text('Connection ID', size =(15, 1)), sg.InputText()],
        [sg.Submit()],
        [sg.Button("receive")],
        [sg.Button("terminate")]
        ]
    window = sg.Window("walkie receiver", layout)
        
    while True:
        event, values = window.read()
        if event == "receive":
            receive_call(values[0]);
        if event == "terminate":
            termination_status = True
        if event == sg.WIN_CLOSED:
            break

    window.close()


main()