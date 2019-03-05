from bottle import static_file, route, run


# http://localhost:1234/show/sample.txt
@route('/show/<file>')
def show(file):
    return static_file(file, root=r'.')


#
@route('/download/<file>')
def download(file):
    return static_file(file, root=r'.', download=file)


run(host="localhost", port=1234, reloader=True, debug=True)
