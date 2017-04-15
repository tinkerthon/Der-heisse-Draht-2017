import bottle
from bottle.ext import sqlite
from datetime import datetime

app = application = bottle.Bottle()
plugin = sqlite.Plugin(dbfile='./scores.sqlite3')
app.install(plugin)

def get_names(db):
    """Hole die Teilnehmerliste aus der Datenbank
       und gib sie als Dictionary zurück"""
    names_list = db.execute('SELECT * FROM names ORDER BY id').fetchall()
    return {id: name if name != '' else '#' + str(id) for (id, name) in names_list}

@app.route('/')
def index():
    """Zeige die Rangliste"""
    return bottle.template('./index.tpl')

@app.route('/scores')
def scores(db):
    """API-Endpunkt: Liefere die Daten der Rangliste im JSON-Format"""
    scores = sorted(db.execute('SELECT * FROM scores').fetchall(), key=lambda score: score['punkte'] / score['anzahl'])
    return dict(
        names = get_names(db),
        scores = [dict(score) for score in scores],
        now = datetime.now().strftime('%Y-%m-%d um %H:%M:%S Uhr')
    )

@app.route('/names')
def names(db):
    """Zeige die Namensliste"""
    names = get_names(db)
    return bottle.template('./names.tpl', names=names)

@app.route('/names', method='POST')
def save_names(db):
    """Speichere die Namensliste in der Datenbank"""
    for id in range(1, 16):
        name = bottle.request.forms.get('names.' + str(id))
        db.execute('REPLACE INTO names (id, name) VALUES (?, ?)', [id, name])
    bottle.redirect('/names')

@app.route('/static/<filename>')
def server_static(filename):
    """Liefere statische Dateien (Bilder, Stylesheets)"""
    return bottle.static_file(filename, root='./static')

class StripPathMiddleware(object):
    """Get that slash out of the request"""

    def __init__(self, a):
        self.a = a

    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    bottle.run(app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=8888,
        debug=True,
        reloader=True
    )
