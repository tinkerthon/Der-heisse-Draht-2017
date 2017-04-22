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

trails = [
    [2, 2, 1, 1, 0],
    [2, 2, 2, 1, 1],
    [2, 2, 2, 2, 2],
    [2, 2, 2, 3, 3],
    [2, 2, 3, 3, 4]
]


def schlaeger():

    global bat_y

    if bat_y > 0 and button_b.was_pressed():
        bat_y -= 1
    elif bat_y < 3 and button_a.was_pressed():
        bat_y += 1

    display.set_pixel(4, bat_y, 9)
    display.set_pixel(4, bat_y + 1, 9)


def ball(x, y):
    display.set_pixel(x, y, 9)


while True:
    current_trail = randint(0, 4)

    for ball_x in range(5):
        display.clear()

        ball(ball_x, ball_y)
        schlaeger()
        sleep(200)

    ball_y = trails[current_trail][ball_x]
    if ball_y not in [bat_y, bat_y + 1]:
        break

    current_trail = 4 - current_trail

    for ball_x in range(4, 0, -1):
        display.clear()

        ball(ball_x, ball_y)
        schlaeger()
        sleep(200)

display.show(Image.SKULL)
