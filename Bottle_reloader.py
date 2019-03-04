from bottle import run, route


@route('/')
def index():
    return ("Hello World from Bottle")


@route('/anothercontextroute')
def anothercontextroute():
    return ("Different context route")

run(host="localhost", port=1234, reloader=True, debug=True)
