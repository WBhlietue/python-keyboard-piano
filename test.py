import numpy as np
import pyaudio

# 设置采样率和声音持续时间
sample_rate = 44100
duration = 5  # seconds

# 计算每个音符的频率
notes = {
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
    'G4': 392.00, 'A4': 440.00, 'B4': 493.88, 'C5': 523.25,
}

# 生成钢琴声波形
def generate_piano_wave(note, duration):
    # 计算每个音符的采样点数
    samples = int(sample_rate * duration)

    # 生成时间数组
    time_array = np.linspace(0, duration, samples, False)

    # 生成正弦波
    frequency = notes[note]
    wave = np.sin(2 * np.pi * frequency * time_array)

    # 添加衰减效果
    fadeout = np.linspace(1, 0, int(0.1 * sample_rate))
    wave[-len(fadeout):] *= fadeout

    return wave

# 生成一段旋律
melody = [
    'C4', 'C4', 'D4', 'C4', 'F4', 'E4',
    'C4', 'C4', 'D4', 'C4', 'G4', 'F4',
    'C4', 'C4', 'C5', 'A4', 'F4', 'E4', 'D4',
    'A4', 'A4', 'A4', 'F4', 'G4', 'F4'
]
# 生成每个音符的波形
waves = [generate_piano_wave(note, 0.5) for note in melody]

# 合并所有波形
full_wave = np.concatenate(waves)

# 初始化PyAudio
p = pyaudio.PyAudio()

# 打开音频流
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=sample_rate,
                output=True)

# 发送波形数据到音频流
stream.write(full_wave.astype(np.float32).tostring())

# 关闭音频流和PyAudio
stream.stop_stream()
stream.close()
p.terminate()
