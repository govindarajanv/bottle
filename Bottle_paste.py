from paste import httpserver

import bottle

app = bottle.default_app()


@app.route('/')
def index():
    return 'This is awesome'


httpserver.serve(app, host='localhost', port=1234)
