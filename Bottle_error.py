from bottle import run, route, error


@route('/')
def index():
    return "Welcome to the Guest Longue"


@error(404)

:
def not_found(error):
    # if authorization fails
    return "<h1>Not Found</h1>"


run(host="localhost", port=1234, debug=True)
