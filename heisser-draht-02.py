# heisser-draht-02.py

from microbit import *
import music

beruehrt = 0
jetzt = 0

while True:
    if button_a.was_pressed():
        music.play(music.POWER_UP)
        display.show(Image(
            "99909:"
            "90909:"
            "90909:"
            "90999:"
            "90000"
        ))
        sleep(1000)

        beruehrt = 0
        jetzt = running_time() // 1000
        display.show(str(beruehrt))

    if pin1.is_touched():
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

    neues_jetzt = running_time() // 1000
    if jetzt > 0 and neues_jetzt > jetzt:
        jetzt = neues_jetzt
        music.pitch(440, 6)
