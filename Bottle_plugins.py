from bottle import run, route, template, install
# pip install bottle_sqlite

from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile=r'/Users/govindarajanv/workstation/programming/python /inventory.db'))


@route('/')
def index():
    return template("Hello {{name}}, Welcome to Bottle", name="User")


@route('/show/<devicename>')
def show_device(db, devicename):
    command = db.execute('SELECT id,os,name from devices where name =?', (devicename,))

    row = command.fetchone()
    if row:
        return template('{{id}},{{name}},{{os}}', id=row['id'], name=row['name'], os=row['os'])
    else:
        return template("The specified device {{name}} does not exist", name=devicename)


run(host="localhost", port=1234, debug=True)
