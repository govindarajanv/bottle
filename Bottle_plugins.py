from bottle import run, route, template, install, request
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


# http://localhost:1234/show?id=1&name=laptop
@route('/show')
def show_query():
    os = request.query.os or None
    id = request.query.id or None
    name = request.query.name or None

    querystring = []
    if os:
        querystring.append('os={}'.format(os))
    if id:
        querystring.append('id={}'.format(id))
    if name:
        querystring.append('name={}'.format(name))

    if len(querystring) == 0:
        return "Invalid query"
    else:
        return ' AND '.join(querystring)


run(host="localhost", port=1234, debug=True)
