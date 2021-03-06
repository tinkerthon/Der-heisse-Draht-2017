#
# Spiele Pong.
# Steuerung: Knopf A (unten), Knopf A (oben)
# Neustart: Knoepfe A+B gleichzeitig
# (c) Olav Schettler @oschettler
#

from microbit import *
from random import randint

bat_y = 0
ball_y = 2
ball_x = 0
current_trail = 2
round = 0

trails = [
    [2, 2, 1, 1, 0],
    [2, 2, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [2, 2, 3, 3, 3],
    [2, 2, 3, 3, 4]
]


def bat():
    '''
    Schlaeger: Check und anzeigen
    '''
    global bat_y

    if bat_y > 0 and button_b.was_pressed():
        bat_y -= 1
    elif bat_y < 3 and button_a.was_pressed():
        bat_y += 1

    display.set_pixel(4, bat_y, 9)


def ball():
    '''
    Ball: Aktuelles Y ermitteln und anzeigen
    '''
    global ball_y

    ball_y = trails[current_trail][ball_x]
    display.set_pixel(ball_x, ball_y, 9)


def action():
    '''
    Innere Spielschleife: Ball, Schlaeger, kurze Pause
    '''
    display.clear()

    ball()
    bat()
    sleep(200)


# Aeussere Schleife: Gesamtes Spiel
while True:

    # Innere Schleife: Ball einmal hin und zurueck
    while True:
        current_trail = randint(0, 4)

        # Ball hin
        for ball_x in range(5):
            action()

        if ball_y != bat_y:
            break

        # ... und zurueck
        for ball_x in range(4, -1, -1):
            action()

        round += 1

    # Ball nicht getroffen: Runde zuende
    while not (button_a.was_pressed() and button_b.was_pressed()):
        display.show(Image.SKULL)
        sleep(200)
        display.show(str(round))

    # Neue Runde
    round = 0
    bat_y = 2
