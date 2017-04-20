from microbit import *
import random

def welche_anzeige():
    '''
    Diese Funktion bestimmt, ob Zahlen oder Bilder angezeigt werden.
    '''
    while True:
        if button_a.was_pressed():
            welche = True
            break
        elif button_b.was_pressed():
            welche = False
            break

    display.show("Z" if zeige_zahl else "B")

    return welche


bilder = [
    Image("00000:00000:00900:00000:00000"),
    Image("90000:00000:00000:00000:00009"),
    Image("90000:00000:00900:00000:00009"),
    Image("90009:00000:00000:00000:90009"),
    Image("90009:00000:00900:00000:90009"),
    Image("90009:00000:90009:00000:90009"),
]

zeige_zahl = welche_anzeige()

while True:
    if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
        zeige_zahl = welche_anzeige()

    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        zahl = random.randint(0, 5)
        if zeige_zahl:
            display.show(str(zahl + 1))
        else:
            display.show(bilder[zahl])