from hardware.keypad import Keypad
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# Pin configuration
ROW_PINS = [18, 23, 25, 12]
COL_PINS = [16, 20, 21]

keypad = Keypad(ROW_PINS, COL_PINS)

def listen_for_keypress():
    print("Select a key")
    while True:
        key = keypad.get_key()
        if key:
            print(key[0])

listen_for_keypress()
