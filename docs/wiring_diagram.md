# Payphone Wiring Diagram

The Raspberry Pi connects to a breakout board that originally connected to the main board of the payphone. The breakout board is connected to the peripherals of the payphone. The Raspberry Pi is connected to the breakout board via a ribbon cable.

## Breakout Board

The breakout board is a custom board that was designed to connect to the main board of the payphone. It uses a standard 20 pin IDC connector for a ribbon cable 

| Pin | GPIO   | Function |
| --- | ------ | -------- |
| 01  | GPIO   | unused   |
| 02  | GPIO   | unused   |
| 03  | GPIO   | unused   |
| 04  | GPIO   | unused   |
| 05  | GPIO   | unused   |
| 06  | GPIO18 | KP01     |
| 07  | GPIO   | unused   |
| 08  | GPIO23 | KP03     |
| 09  | GPIO16 | KP02     |
| 10  | GPIO25 | KP05     |
| 11  | GPIO20 | KP04     |
| 12  | GPIO12 | KP07     |
| 13  | GPIO13 | KP06     |
| 14  | GPIO   | unused   |
| 15  | GPIO   | unused   |
| 16  | GPIO   | unused   |
| 17  | GPIO   | unused   |
| 18  | GPIO   | unused   |
| 19  | GPIO   | unused   |
| 20  | GPIO   | unused   |

## Keypad

The keypad uses a standard 3x4 matrix pattern found on most phone-style keypads. The keypad is directly connected into the back of the breakout board.

| Pin | Type   | Breakout Board Pin |
| --- | ------ | ------------------ |
| 01  | Row    | BB06               |
| 02  | Column | BB09               |
| 03  | Row    | BB08               |
| 04  | Column | BB11               |
| 05  | Row    | BB10               |
| 06  | Column | BB13               |
| 07  | Row    | BB12               |
| 08  | ---    | unused             |
| 09  | ---    | unused             |
| 10  | ---    | unused             |