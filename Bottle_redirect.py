from bottle import run, route, redirect


@route('/')
def index():
    return "Please authorize yourself"


@route('/guest')
def index():
    return "Welcome to the Guest Longue"


@route('/restrictedArea')
def restricted():
    # if authorization fails
    redirect("/")


@route('/unRestrictedArea')
def restricted():
    # No Authorization required
    redirect("/guest")


run(host="localhost", port=1234, debug=True)
