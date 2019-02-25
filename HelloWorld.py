from bottle import run, route


@route('/')
def index():
    return ("Hello World from Bottle")


run(host="localhost", port=1234, debug=True)

