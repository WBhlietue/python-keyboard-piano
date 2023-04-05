from pynput import keyboard
import winsound
import pyaudio
import numpy as np

pressed_keys = set()

uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sample_rate = 44100
duration = 0.1

n_samples = int(sample_rate * duration)
time_array = np.arange(n_samples) / float(sample_rate)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                output=True)


def GetIndex(char):
    if(char in uppercase_letters):
        return uppercase_letters.index(char)
    elif (char in lowercase_letters):
        return lowercase_letters.index(char)
    else:
        return -1


def Play():
    winsound.Beep(440, 90)

def press_down(key):
    try:
        freq = 50*(GetIndex(key.char) + 5) # 音符的频率，这里为 A4
        audio_signal = np.sin(2.0 * np.pi * freq * time_array)
        stream.write(audio_signal.astype(np.float32).tostring())
        # winsound.Beep(50*(GetIndex(key.char) + 5), 90)
        pass
    except:
        pass
    pass

def on_press(key):
    if  not (key in pressed_keys):
        pressed_keys.add(key)
        press_down(key)

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
