import RPi.GPIO as GPIO

# defines the 12 key, 7 pin phone keypad
class Keypad:
    def __init__(self, row_pins, col_pins):
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
        GPIO.setmode(GPIO.BCM)

    def get_key(self):
        for j in range(len(self.col_pins)):
            GPIO.setup(self.col_pins[j], GPIO.OUT)
            GPIO.output(self.col_pins[j], GPIO.LOW)

        for i in range(len(self.row_pins)):
            GPIO.setup(self.row_pins[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        for j in range(len(self.col_pins)):
            GPIO.setup(self.col_pins[j], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            for i in range(len(self.row_pins)):
                if GPIO.input(self.row_pins[i]) == 0:
                    return [self.keypad[i][j], self.toneMap[i][j]]

            GPIO.setup(self.col_pins[j], GPIO.IN, pull_up_down=GPIO.PUD_UP)

        return None

    def cleanup(self):
        GPIO.cleanup()


