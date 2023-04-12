from pynput import keyboard
import pygame.midi
import pygame

pressed_keys = set()

# uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z',
                     'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', ';', ',', '.', '/']
lowercase_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
                    's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
pygame.midi.init()

pygame.midi.get_device_info(0)

player = pygame.midi.Output(0)

player.set_instrument(0)


def GetIndex(char):
    if(char in uppercase_letters):
        return uppercase_letters.index(char)
    elif (char in lowercase_letters):
        return lowercase_letters.index(char)
    else:
        return -1


def press_down(key):
    try:
        player.note_on(40+GetIndex(key.char), 127, 0)
        pass
    except:
        pass
    pass


def on_press(key):
    # player.note_on(40+GetIndex(key.char), 127)
    if not (key in pressed_keys):
        pressed_keys.add(key)
        press_down(key)


def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


# import pygame.midi
# import time

# # 初始化 Pygame MIDI 模块
# pygame.midi.init()

# # 打开默认 MIDI 输出设备
# player = pygame.midi.Output(0)

# # 选择乐器
# player.set_instrument(0)

# # 播放 C4 音符，持续时间为一秒钟
# player.note_on(60, 127)  # MIDI 数字 60 表示 C4 音符，127 表示最大音量
# time.sleep(1)
# player.note_off(60, 0)

# # 关闭 MIDI 输出设备
# player.close()

# # 退出 Pygame MIDI 模块
# pygame.midi.quit()
