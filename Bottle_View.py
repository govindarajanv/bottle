from bottle import run, route, template, view


@route('/')
@view('hello_template')
def index():
    return dict(name="User")


run(host="localhost", port=1234, debug=True)

