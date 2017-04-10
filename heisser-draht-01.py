# heisser-draht-01.py

from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image(
            "99909:"
            "90909:"
            "90909:"
            "90999:"
            "90000"
        ))
        sleep(1000)

        beruehrt = 0
        display.show(str(beruehrt))

    if pin0.is_touched():
        display.show(Image(
            "90009:"
            "09090:"
            "00900:"
            "09090:"
            "90009"
        ))
        sleep(1000)

        beruehrt += 1

        display.show(str(beruehrt))
