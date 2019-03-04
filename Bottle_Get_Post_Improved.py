from bottle import request, run, route


@route('/', method=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return "GET using Bottle: This is your response"
    elif request.method == 'POST':
        return "You have passed 1234"
    elif request.method == 'DELETE':
        return "Welcome to delete operation using Bottle framework"


run(host="localhost", port=1234, debug=True)
