import bottle
from bottle.ext import sqlite
from datetime import datetime

app = bottle.Bottle()
plugin = sqlite.Plugin(dbfile='./scores.sqlite3')
app.install(plugin)

namen = {
    1: 'Olav'
}

@app.route('/')
def index():
    return bottle.template('./index.tpl')

@app.route('/scores')
def scores(db):
    scores = db.execute('SELECT * FROM scores ORDER BY rang').fetchall()
    return dict(
        namen=namen,
        scores=[dict(score) for score in scores],
        jetzt=datetime.now().strftime('%Y-%m-%d um %H:%M:%S Uhr')
    )

@app.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='./static')

if __name__ == '__main__':
    app.run(host='localhost', port=8888, debug=True, reloader=True)
