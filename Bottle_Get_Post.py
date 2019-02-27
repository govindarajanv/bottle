from bottle import get, post, delete, run, route


@get('/')
def index_get():
    return "Post using Bottle: This is your response"


@post('/')
def index_post():
    return "You have passed 1234"


@delete('/')
def index_delete():
    return "Welcome to delete operation using Bottle framework"


run(host="localhost", port=1234, debug=True)
