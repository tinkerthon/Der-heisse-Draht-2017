# heisser-draht-03.py

from microbit import *
import music

beruehrt = 0
jetzt = 0


def knopf_a():
    '''
    Knopf A startet das Spiel
    '''

    global beruehrt, start, jetzt

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
    start = jetzt = running_time() // 1000
    display.show(str(beruehrt))


def knopf_b():
    '''
    Knopf B beendet das Spiel
    '''

    global jetzt

    music.play(music.POWER_DOWN)
    display.scroll(
        str(beruehrt) + ':' +
        str(jetzt - start) + '=' +
        str(jetzt - start + beruehrt * 5)
    )
    jetzt = 0


def draht_beruehrt():

    global beruehrt

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


def tick():

    global neues_jetzt, jetzt

    display.scroll(str(beruehrt) + str(jetzt))

    neues_jetzt = running_time() // 1000
    if jetzt > 0 and neues_jetzt > jetzt:
        jetzt = neues_jetzt
        music.pitch(440, 6)


while True:
    if button_a.was_pressed():
        knopf_a()

    if button_b.was_pressed():
        knopf_b()

    if pin1.is_touched():
        draht_beruehrt()

    tick()
