# Der heiße Draht 2017

![Open Educational Resource](http://www.unesco.org/webworld/download/oer/EN/oer_logo_EN_2.png)

Materialien zum [Physical Computing Workshop 2017](http://www.deutsches-museum.de/bonn/information/fuer-kinder-und-schulen/die-kleine-eule-pfiffikus/workshops/der-heisse-draht/) im Deutschen Museum in Bonn.

## Entwicklungsstufen des MicroPython-Programmes für den Micro:bit

Das Programm dient als Spielsteuerung für das Spiel "Der heiße Draht"

* heisser-draht-01.py - Zählen von Berührungen
* heisser-draht-02.py - Zusätzlich Zeitmessung
* heisser-draht-03.py - Zusätzlich Anzeige von Berührungen und Zeit
* heisser-draht-04.py - Senden der Ergebnisse mit radio.send()
* heisser-draht-05.py - Bereinigung, Eingabe einer Spieler-ID

## Ablauf

Das Programm `log.py` läuft auf einem weiteren Micro:bit und empfängt die Spielergebnisse. `scores.py` empfängt diese Spielstände über eine serielle Verbindung und schreibt sie in eine SQlite-Datenbank.

Die Web-Anwendung in `leaderboard` stellt die Spielergebnisse als Rangliste dar. Hierüber können auch die Teilnehmernamen in der Datenbank zur Anzeige gepflegt werden.

## Workshop-Konzept

Zum Workshop gibt es ein [umfassendes Konzept](workshop-konzept.pdf). Das Konzept steht unter der der Lizenz [Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/) und kann gerne für eigene Veranstaltungen genutzt werden. Ich freue mich natürlich über [Änderungs- oder Verbesserungsvorschläge](https://olav.net/contact). 

## Weitere Links zum Micro:bit mit MicroPython

* [Darryl Sloan](https://www.youtube.com/watch?v=YooBM1gOMuo) demonstriert ein "Alien"-Spiel, geschrieben in MicroPython. Er schreibt ein [Buch mit Programmieranleitungen](https://www.facebook.com/microgamesbook/) zu weiteren Spielen
* [David Whale](https://twitter.com/whaleygeek) hat einige Spiele und viele [weitere Spielideen](https://github.com/whaleygeek/microbit_python/blob/master/game_ideas.txt) in [seinem Github-Repo](https://github.com/whaleygeek/microbit_python).
* [Pete Dring](https://plus.google.com/+pddring) hat einen Micro:bit [MicroPython-Simulator](https://create.withcode.uk/) und viele Spiele-Anleitungen, u.a. [Doodle Jump](http://blog.withcode.uk/2016/06/doodle-jump-microbit-python-game-tutorial/)
