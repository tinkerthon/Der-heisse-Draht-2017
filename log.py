# A micro:bit Firefly.
import radio
from microbit import *

radio.on()

while True:
    incoming = radio.receive()
    if (incoming != None):
        print(str(running_time()) + ': ' + incoming)
