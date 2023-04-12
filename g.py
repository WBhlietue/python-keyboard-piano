import numpy as np
import pyaudio
import time

# 钢琴键频率
PITCHES = {
    'A0': 27.5,
    'C1': 32.7032,
    'D#1': 38.8909,
    'F#1': 46.2493,
    'A1': 55,
    'C2': 65.4064,
    'D#2': 77.7817,
    'F#2': 92.4986,
    'A2': 110,
    'C3': 130.8128,
    'D#3': 155.5635,
    'F#3': 184.9972,
    'A3': 220,
    'C4': 261.6256,
    'D#4': 311.1270,
    'F#4': 369.9944,
    'A4': 440,
    'C5': 523.2511,
    'D#5': 622.2540,
    'F#5': 739.9888,
    'A5': 880,
    'C6': 1046.502,
    'D#6': 1244.508,
    'F#6': 1479.978,
    'A6': 1760,
    'C7': 2093.005,
    'D#7': 2489.016,
    'F#7': 2959.955,
    'A7': 3520,
    'C8': 4186.009,
    'D#8': 4978.032,
    'D4':600
}

# 生成钢琴波形
def generate_piano_wave(frequency, duration):
    # 每秒采样点数
    sample_rate = 44100
    # 每个采样点的时间间隔
    time_steps = np.linspace(0, duration, int(sample_rate * duration), False)
    # 生成正弦波
    wave = np.sin(frequency * 2 * np.pi * time_steps)
    # 钢琴音的衰减和淡入淡出效果
    envelope = np.concatenate([
        np.linspace(0, 1, int(0.1 * sample_rate), False),
        np.linspace(1, 0.7, int(0.1 * sample_rate), False),
        np.linspace(0.7, 0.7, int(0.8 * sample_rate), False)
    ])
    wave *= envelope
    # 限制波形的振幅范围（避免产生过大的振幅）
    wave = np.clip(wave, -1, 1)
    return wave.astype(np.float32)

# 播放音符
def play_note(note, duration):
    # 获取频率
    frequency = PITCHES[note]
    # 生成波形
    wave = generate_piano_wave(frequency, duration)
    # 播放波形
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)
    stream.write(wave.tobytes())
    time.sleep(duration)
    stream.stop_stream()
    stream.close()
    p.terminate()
def play_song():
    song = [('C4', 1), ('C4', 1), ('D4', 1), ('C4', 1), ('F4', 1), ('E4', 1), ('C4', 1), ('C4', 1), ('D4', 1), ('C4', 1), ('G4', 1), ('F4', 1), ('C4', 1), ('C4', 1), ('C5', 1), ('A4', 1), ('F4', 1), ('E4', 1), ('D4', 1), ('A4', 1), ('A4', 2), ('G4', 1), ('F4', 1), ('C4', 1), ('C4', 1), ('C5', 1), ('A4', 1), ('F4', 1), ('E4', 1), ('D4', 1), ('G4', 1), ('F4', 1)]
    for note, duration in song:
        play_note(note, duration)

play_song()