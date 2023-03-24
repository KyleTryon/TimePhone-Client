import platform
if platform.system() == 'Windows':
    from hardware.emulateKeypad import Keypad
else:
    from hardware.keypad import Keypad

from services.call_service import CallService

import threading

# Pin configuration
ROW_PINS = [18, 23, 25, 12]
COL_PINS = [16, 20, 21]

keypad = Keypad(ROW_PINS, COL_PINS)
call_service = CallService()

def listen_for_keypress():
    print("Select a key")
    while True:
        # if emulator then check if keypad thread has stopped, if it has break the loop
        if keypad.emulator:
            if not keypad.thread.is_alive():
                break
        key = keypad.get_key()
        if key:
            phone_number = ''.join(keypad.history)
            call_service.dial(phone_number)

keypad_thread = threading.Thread(target=listen_for_keypress)
keypad_thread.start()
