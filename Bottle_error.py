from bottle import run, route, error, abort


@route('/')
def index():
    return "Welcome to the Guest Longue"


@error(404)
def not_found(error):
    # if authorization fails
    return "<h1>Not Found</h1>"


@error(401)
def not_found(error):
    # 401 is handled
    return "<h1>Validation Failed. Please try again</h1>"


@route('/validationFailed')
def validationFailure():
    # throws 401
    abort(401)


run(host="localhost", port=1234, debug=True)
