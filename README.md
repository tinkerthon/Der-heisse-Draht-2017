# Der heiße Draht 2017

Materialien zum Physical Computing Workshop 2017 im Deutschen Museum in Bonn.

# Entwicklungsstufen des MicroPython-Programmes für den Micro:bit

Das Programm dient als Spielsteuerung für das Spiel "Der heiße Draht"

* heisser-draht-01.py - Zählen von Berührungen
* heisser-draht-02.py - Zusätzlich Zeitmessung
* heisser-draht-03.py - Zusätzlich Anzeige von Berührungen und Zeit
* heisser-draht-04.py - Senden der Ergebnisse mit radio.send()
* heisser-draht-05.py - Bereinigung, Eingabe einer Spieler-ID

Das Programm `log.py` läuft auf einem weiteren Micro:bit und empfängt die Spielergebnisse. `scores.py` empfängt diese Spielstände über eine serielle Verbindung und schreibt sie in eine SQlite-Datenbank.

Die Web-Anwendung in `leaderboard` stellt die Spielergebnisse als Rangliste dar. Hierüber können auch die Teilnehmernamen in der Datenbank zur Anzeige gepflegt werden.

Zum Workshop gibt es ein umfassendes Konzept. Bei Interesse bitte [Nachricht an mich](https://tinkerthon.de/impressum/).
