import sqlite3
db = sqlite3.connect('./scores.sqlite3')
db.execute("CREATE TABLE scores (id INTEGER PRIMARY KEY, anzahl INTEGER, zeit INTEGER, beruehrt INTEGER, punkte INTEGER)")
db.execute("INSERT INTO scores (id, anzahl, zeit, beruehrt, punkte) VALUES (1, 3, 42, 5, 67)")
db.execute("CREATE TABLE names (id INTEGER PRIMARY KEY, name STRING)")
db.execute("INSERT INTO names (id, name) VALUES (1, 'Olav')")
db.commit()
