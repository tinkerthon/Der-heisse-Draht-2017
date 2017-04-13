import sqlite3
db = sqlite3.connect('./scores.sqlite3')
db.execute("CREATE TABLE scores (id INTEGER PRIMARY KEY, anzahl INTEGER, zeit INTEGER, beruehrt INTEGER, rang INTEGER)")
db.execute("INSERT INTO scores (id, anzahl, zeit, beruehrt, rang) VALUES (1, 3, 42, 5, 1)")
db.execute("CREATE TABLE names (id INTEGER PRIMARY KEY, name STRING)")
db.execute("INSERT INTO names (id, name) VALUES (1, 'Olav')")
db.commit()
