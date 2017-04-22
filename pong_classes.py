#
# Spiele Pong.
# Steuerung: Knopf A (unten), Knopf A (oben)
# Neustart: Knoepfe A+B gleichzeitig
# (c) Olav Schettler @oschettler
#

from microbit import *
from random import randint

class Bat:  
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
        print("Round:", self.round, "Ball:", self.ball.y, "Bat:", self.bat.y)
        sleep(300)

    
    def run(self):
        self.ball.current_trail = randint(0, 4)

        # Ball hin
        for self.ball.x in range(5):
            self.action()

        if self.ball.y != self.bat.y:
            # nicht getroffen. Game over
            return False

        # ... und zurueck
        for self.ball.x in range(4, -1, -1):
            self.action()

        self.round += 1
        
        # naechste Runde
        return True
        
        
    def over(self):
        # Ball nicht getroffen: Runde zuende
        while not (button_a.was_pressed() and button_b.was_pressed()):
            display.show(Image.SKULL)
            sleep(200)
            display.show(str(self.round))
            sleep(1000)


# Zeige 'Pg' (fuer "Pong") und warte auf Tasten A+B
display.show(Image('99099:90909:99099:90009:90099'))
while not (button_a.was_pressed() and button_b.was_pressed()):
    pass

# Aeussere Schleife: Gesamtes Spiel
while True:
    game = Game()

    while game.run():
        pass
        
    game.over()
