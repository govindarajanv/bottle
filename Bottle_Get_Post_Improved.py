from bottle import requests, run, route


@route('/', method=['GET', 'POST', 'DELETE'])
def index():
    if requests.method == 'GET':
        return "GET using Bottle: This is your response"
    elif requests.method == 'POST':
        return "You have passed 1234"
    elif requests.method == 'DELETE':
        return "Welcome to delete operation using Bottle framework"


run(host="localhost", port=1234, debug=True)
