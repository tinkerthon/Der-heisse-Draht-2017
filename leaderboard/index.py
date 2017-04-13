import bottle
from bottle.ext import sqlite
from datetime import datetime

app = bottle.Bottle()
plugin = sqlite.Plugin(dbfile='./scores.sqlite3')
app.install(plugin)

def get_names(db):
    names_list = db.execute('SELECT * FROM names ORDER BY id').fetchall()
    return {id: name for (id, name) in names_list}

@app.route('/')
def index():
    return bottle.template('./index.tpl')

@app.route('/scores')
def scores(db):
    scores = db.execute('SELECT * FROM scores ORDER BY rang').fetchall()
    return dict(
        names = get_names(db),
        scores = [dict(score) for score in scores],
        now = datetime.now().strftime('%Y-%m-%d um %H:%M:%S Uhr')
    )

@app.route('/names')
def names(db):
    names = get_names(db)
    return bottle.template('./names.tpl', names=names)

@app.route('/names', method='POST')
def save_names(db):
    for id in range(1, 16):
        name = bottle.request.forms.get('names.' + str(id))
        db.execute('REPLACE INTO names (id, name) VALUES (?, ?)', [id, name])
    bottle.redirect('/names')

@app.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='./static')

if __name__ == '__main__':
    app.run(host='localhost', port=8888, debug=True, reloader=True)
