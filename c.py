import pygame.midi
import time

# 初始化 Pygame MIDI 模块
pygame.midi.init()

# 打开默认 MIDI 输出设备
player = pygame.midi.Output(0)

# 选择乐器
player.set_instrument(0)

# 播放 C4 音符，持续时间为一秒钟
player.note_on(60, 127)  # MIDI 数字 60 表示 C4 音符，127 表示最大音量
time.sleep(1)
player.note_off(60, 0)

# 关闭 MIDI 输出设备
player.close()

# 退出 Pygame MIDI 模块
pygame.midi.quit()
