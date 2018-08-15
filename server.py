from flask import Flask, render_template, g
import sqlite3
from contextlib import closing

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

@app.route('/')
def index():
    # cur = g.db.execute('select * from servers order by name')
    # server_list = [dict(id=row[0], serverName=row[1], status=isAlive(row[1])) for row in cur.fetchall()]
    # return render_template('index.html', server_list=server_list)
    return render_template('index.html')

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def isAlive(servername):
    # ping server (or do sth) to check if a server is alive or not
    return 0  #easy first

@app.route('/login')
def login(username='admin'):
    cur = g.db.execute('select * from users where username=\'{}\' order by username'.format(username))
    return cur
    #cur.fetchall()

if __name__ == '__main__':
    app.run()