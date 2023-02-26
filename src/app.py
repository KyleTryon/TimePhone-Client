from hardware.keypad import Keypad
import threading

# Pin configuration
ROW_PINS = [1, 2, 3, 4]
COL_PINS = [5, 6, 7]

keypad = Keypad(ROW_PINS, COL_PINS)

# On a separate thread, listen for key presses
def listen_for_keypress():
    while True:
        key = keypad.get_key()
        if key:
            print(key[0])

thread = threading.Thread(target=listen_for_keypress)
thread.start()