# heisser-draht-05.py

from microbit import *
import music
import radio

beruehrt = 0
jetzt = 0
start = 0

radio.on()

display.show(Image(
    "90990:"
    "90909:"
    "90909:"
    "90909:"
    "90990"
))
sleep(1000)

id = 1
while not button_b.was_pressed():
    display.show(str(id))
    if button_a.was_pressed():
        id += 1
    if id > 15:
        id = 1

music.play(music.BA_DING)

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
        button_b.was_pressed()
        
        start = jetzt = running_time() // 1000
        display.show(str(beruehrt))

    if jetzt > 0 and button_b.was_pressed():
        ergebnis = str(id) + ':' + str(beruehrt) + ':' + str(jetzt - start) + ':' + str(jetzt - start + beruehrt * 5)
        print(ergebnis)

        radio.send(ergebnis)

        music.play(music.POWER_DOWN)
        display.scroll(ergebnis)
        jetzt = 0
        
        sleep(1000)
        display.show(str(id))

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
