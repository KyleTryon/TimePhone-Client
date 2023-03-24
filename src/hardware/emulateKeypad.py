from tkinter import *
import tkinter as tk

import threading
import time

class Keypad():
       
        
    def __init__(self, row_pins, col_pins):
        self.start()
        self.keypad_event = threading.Event()
        self.history = []


    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.wm_title("Keypad Emulator")
        self.root.protocol("WM_DELETE_WINDOW", self.callback)


        # create keypad buttons
        self.button1 = tk.Button(self.root, text="1", command=lambda: self.button_press("1"))
        self.button2 = tk.Button(self.root, text="2", command=lambda: self.button_press("2"))
        self.button3 = tk.Button(self.root, text="3", command=lambda: self.button_press("3"))
        self.button4 = tk.Button(self.root, text="4", command=lambda: self.button_press("4"))
        self.button5 = tk.Button(self.root, text="5", command=lambda: self.button_press("5"))
        self.button6 = tk.Button(self.root, text="6", command=lambda: self.button_press("6"))
        self.button7 = tk.Button(self.root, text="7", command=lambda: self.button_press("7"))
        self.button8 = tk.Button(self.root, text="8", command=lambda: self.button_press("8"))
        self.button9 = tk.Button(self.root, text="9", command=lambda: self.button_press("9"))
        self.button0 = tk.Button(self.root, text="0", command=lambda: self.button_press("0"))
        self.buttonStar = tk.Button(self.root, text="*", command=lambda: self.button_press("*"))
        self.buttonPound = tk.Button(self.root, text="#", command=lambda: self.button_press("#"))

        # add a call button
        self.buttonCall = tk.Button(self.root, text="Call", command=lambda: self.button_press("Call"))
        self.buttonCall.grid(row=4, column=0, columnspan=3)

        # create keypad buttons
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.button0.grid(row=3, column=1)
        self.buttonStar.grid(row=3, column=0)
        self.buttonPound.grid(row=3, column=2)

        self.root.mainloop()
        
    def button_press(self, key):
        print(key)
        self.keypad_event.set()
        self.key = key
        # add key to history
        self.history.append(key)
        # if call button is pressed, clear history
        if key == "Call":
            self.history = []
        
        
    def cleanup(self):
        self.root.destroy()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.root.destroy()
        self.thread.join()

    def get_key(self):
        if self.keypad_event.wait(0.1):
            self.keypad_event.clear()
            return self.key
        else:
            return None
        


if __name__ == "__main__":
    keypad = Keypad()
    time.sleep(10)
    keypad.cleanup()


    
    
    
            
        
        
        

        

