#
# Spiele Pong.
# Steuerung: Knopf A (unten), Knopf A (oben)
# Neustart: Knoepfe A+B gleichzeitig
# (c) Olav Schettler @oschettler
#

from microbit import *
from random import randint

class Bat:
    x
    y
    
    def __init__(self):
        self.y = 2
    
    def run(self):
        '''
        Schlaeger: Check und anzeigen
        '''
        if self.y > 0 and button_b.was_pressed():
            self.y -= 1
        elif self.y < 3 and button_a.was_pressed():
            self.y += 1

        display.set_pixel(4, self.y, 9)


class Ball:
    x
    y
    current_trail
    trails = [
        [2, 2, 1, 1, 0],
        [2, 2, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [2, 2, 3, 3, 3],
        [2, 2, 3, 3, 4]
    ]
    
    def run(self):
        '''
        Ball: Aktuelles Y ermitteln und anzeigen
        '''
        self.y = self.trails[self.current_trail][self.x]
        display.set_pixel(self.x, self.y, 9)


class Game:
    ball
    bat
    round
    
    def __init__(self):
        self.ball = Ball()
        self.bat = Bat()
        self.round = 0

    
    def action(self):
        '''
        Innere Spielschleife: Ball, Schlaeger, kurze Pause
        '''
        display.clear()

        self.ball.run()
        self.bat.run()
        sleep(200)

    
    def round(self):
        self.ball.current_trail = randint(0, 4)

        # Ball hin
        for self.ball.x in range(5):
            self.action()

        if self.ball.y != self.bat.y:
            return False

        # ... und zurueck
        for self.ball.x in range(4, -1, -1):
            self.action()

        self.round += 1
        
        
    def over(self):
        # Ball nicht getroffen: Runde zuende
        while not (button_a.was_pressed() and button_b.was_pressed()):
            display.show(Image.SKULL)
            sleep(200)
            display.show(str(self.round))


# Aeussere Schleife: Gesamtes Spiel
while True:
    game = Game()

    while game.round():
        pass
        
    game.over()
