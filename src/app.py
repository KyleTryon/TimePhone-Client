from hardware.keypad import Keypad
from services.call_service import CallService
import RPi.GPIO as GPIO
import threading

GPIO.setwarnings(False)
# Pin configuration
ROW_PINS = [18, 23, 25, 12]
COL_PINS = [16, 20, 21]

keypad = Keypad(ROW_PINS, COL_PINS)
call_service = CallService()

def listen_for_keypress():
    print("Select a key")
    while True:
        key = keypad.get_key()
        if key:
            phone_number = ''.join(keypad.history)
            call_service.dial(phone_number)

keypad_thread = threading.Thread(target=listen_for_keypress)
keypad_thread.start()

