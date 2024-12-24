import os
import time
import random
import threading
from pynput import keyboard
import pyautogui

# The paragraph you want to type out
paragraph = """
Your paragraph goes here. Replace this text with the paragraph you want the script to type out.
"""

# Global variables to control the typing state
is_typing = False
is_paused = False
current_keys = set()

def type_paragraph():
    global is_typing, is_paused
    words = paragraph.split()
    index = 0
    while is_typing and index < len(words):
        if is_paused:
            time.sleep(0.1)
            continue

        word = words[index]

        # Simulate human-like delay before typing the word
        time.sleep(random.uniform(0.2, 0.5))

        # Simulate typing with possible mistakes
        simulate_typing(word + ' ')

        index += 1

    is_typing = False  # Reset typing state when done

def simulate_typing(text):
    for char in text:
        # Random chance to make a typo
        if random.random() < 0.1:
            typo_char = random.choice('abcdefghijklmnopqrstuvwxyz')
            pyautogui.typewrite(typo_char)
            time.sleep(random.uniform(0.05, 0.15))
            # Backspace to correct the typo
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.15))

        # Type the correct character
        pyautogui.typewrite(char)
        # Random delay between keystrokes to simulate human typing
        time.sleep(random.uniform(0.05, 0.2))

def on_press(key):
    global is_typing, is_paused, current_keys
    try:
        current_keys.add(key)

        if keyboard.Key.cmd in current_keys or keyboard.Key.ctrl in current_keys:
            # Start typing with cmd + a + w
            if keyboard.KeyCode.from_char('a') in current_keys and keyboard.KeyCode.from_char('w') in current_keys:
                if not is_typing:
                    is_typing = True
                    is_paused = False
                    threading.Thread(target=type_paragraph).start()
            # Pause typing with cmd + a
            elif keyboard.KeyCode.from_char('a') in current_keys and len(current_keys) == 2:
                is_paused = True
            # Continue typing with cmd + w
            elif keyboard.KeyCode.from_char('w') in current_keys and len(current_keys) == 2:
                if is_typing:
                    is_paused = False

    except AttributeError:
        pass  # Handle special keys that don't have a char attribute

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass
    # Stop listener if escape is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

3ddwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwrt    # This is the text I typed out manually                                                                                                                                                                                                                                                                         xdr
zė6r                                            ßd5AZwwwwwwwwwŻ                                                                                                                                                                                                                                              xdr                                                                                                                                                        SCWwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwTSwwwwwwwwwwwEYSRwwwwwwwwwwwX5ZTÃ
