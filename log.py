# Protokolliere Spielergebnisse

import radio
from microbit import *

radio.on()

while True:
    incoming = radio.receive()
    if (incoming != None):
        print(incoming)
