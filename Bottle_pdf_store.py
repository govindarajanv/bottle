from bottle import run, route, template, get, post, request
import os


@route('/')
def index():
    return template('index', uploads=os.listdir(r'./uploads'))


@get('/upload')
def upload():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
          Select a file: <input type="file" name="upload" multiple />
          <input type="submit" value="Start upload" />
        </form>
            '''


@post('/upload')
def upload():
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)

    if not ext in ('.jpg', '.png', '.pdf'):
        return "File type {} not supported".format(ext)

    path = r'./uploads'
    upload.save(path, overwrite=True)
    return 'OK'


run(host="localhost", port=1234, debug=True)
