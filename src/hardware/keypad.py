import RPi.GPIO as GPIO
from typing import List
import time
# defines the 12 key, 7 pin phone keypad
class Keypad:
    def __init__(self, row_pins, col_pins):
        GPIO.setwarnings(False)
        self.debounceTime = 20 / 1000.0
        self.row_pins = row_pins
        self.col_pins = col_pins
        self.keypad = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]
        self.toneMap = [
            [[1209, 697],[1336, 697],[1477, 697]],
            [[1209, 770],[1336, 770],[1477, 770]],
            [[1209, 852],[1336, 852],[1477, 852]],
            [[1209, 941],[1336, 941],[1477, 941]]
        ]
        self.history: List[str] = []
        GPIO.setmode(GPIO.BCM)

    def get_key(self):
        # Set up rows as inputs with pull-up resistors
        for row_pin in self.row_pins:
            GPIO.setup(row_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Set up columns as outputs
        for col_pin in self.col_pins:
            GPIO.setup(col_pin, GPIO.OUT)

        # Scan each column
        for i, col_pin in enumerate(self.col_pins):
            # Set column output low
            GPIO.output(col_pin, GPIO.LOW)

            # Scan each row
            for j, row_pin in enumerate(self.row_pins):
                # Check if key is pressed
                if not GPIO.input(row_pin):
                    # Wait for key release
                    time.sleep(self.debounceTime)
                    while not GPIO.input(row_pin):
                        time.sleep(self.debounceTime)
                    self._set_key_history(self.keypad[j][i])
                    return self.keypad[j][i]

            # Set column output high
            GPIO.output(col_pin, GPIO.HIGH)

            # Wait for column to settle
            time.sleep(self.debounceTime)
    # The key history records the last 10 keys pressed. The order is oldest to newest.
    def _set_key_history(self, key):
        if len(self.history) >= 10:
            self.history.pop(0)
        self.history.append(key)
    def cleanup(self):
        GPIO.cleanup()
