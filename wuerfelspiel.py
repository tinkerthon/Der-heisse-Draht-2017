from microbit import *
import music

gesuchte_zahl = 1

while True:
    if button_a.was_pressed():
        gesuchte_zahl = gesuchte_zahl + 1
    if gesuchte_zahl > 8:
        gesuchte_zahl = 1
        
    display.show(str(gesuchte_zahl))
 
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        zahl = random.randint(1, 8)

        display.show(str(zahl))
        sleep(2000)
        
        if gesuchte_zahl == zahl:
            display.show(Image.HAPPY)
            music.play(music.POWER_UP)
        elif gesucht_zahl % 2 == zahl % 2:
            display.show(Image.YES)
            music.play(music.JUMP_UP)
        else:
            display.show(Image.SKULL)
            music.play(music.WAWAWAWAA)
