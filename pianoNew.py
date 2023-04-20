from pynput import keyboard
import pygame.midi
import pygame
print("\n\n\n\npress ani key to start")

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

player.set_instrument(1)


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

