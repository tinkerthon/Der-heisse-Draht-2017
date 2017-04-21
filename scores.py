# Empfange Spielergebnisse und aktualisiere die Rangliste
# https://microbit-playground.co.uk/howto/GUIZero-pySerial-microbit-how-to-connect
import serial
from serial.tools import list_ports
import sqlite3
db = sqlite3.connect('./leaderboard/scores.sqlite3')
db.row_factory = sqlite3.Row

def find_microbit_comport():
    ports = list(list_ports.comports())
    for p in ports:
        if (p.pid == 516) and (p.vid == 3368):
            return str(p.device)


def save_score(new_score):
    id = new_score[0]

    score = db.execute('SELECT * FROM scores WHERE id = ?', [id]).fetchone()

    if score:
        anzahl = score['anzahl'] + 1
        beruehrt = score['beruehrt'] + int(new_score[1])
        zeit = score['zeit'] + int(new_score[2])
        punkte = score['punkte'] + int(new_score[1]) * 5 + int(new_score[2])

        db.execute('UPDATE scores SET anzahl=?, beruehrt=?, zeit=?, punkte=? WHERE id=?', [anzahl, beruehrt, zeit, punkte, id])
    else:
        anzahl = 1
        beruehrt = new_score[1]
        zeit = new_score[2]
        punkte = int(new_score[1]) * 5 + int(new_score[2])

        db.execute('INSERT INTO scores (id, anzahl, beruehrt, zeit, punkte) VALUES (?,?,?,?,?)', [id, anzahl, beruehrt, zeit, punkte])

    db.commit()


if __name__ == '__main__':

    ser = serial.Serial()
    ser.baudrate = 115200

    port = find_microbit_comport()
    print("Micro:bit ist an " + port)
    ser.port = port
    ser.open()

    while True:
        # Felder: User-ID, Anz. Ber�hrungen, Zeit, Punkte
        score = ser.readline().decode().strip().split(':')
        print("Score:", score)
        save_score(score)
