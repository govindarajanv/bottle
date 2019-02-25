from bottle import run, route, template


@route('/')
def index():
    return template("Hello {{name}}, Welcome to Bottle", name="User")


run(host="localhost", port=1234, debug=True)
