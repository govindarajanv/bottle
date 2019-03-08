# from bottle import get, post, route, request, response, redirect, run
from bottle import get, post, delete, run, route, request, response, redirect

allowed_account = ['admin', 'user', 'poweruser']


@get('/')
def index():
    return '''
       <form action="/" method="post"> 
          Username: <input type="text" name="username"/>
          Password: <input type="password" name="password"/>
          <input type="submit" value="Login" />
        </form>
       '''


@post('/')
def index():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print(username)
    print(password)
    if username == "admin" and password == "password":
        response.set_cookie('account', username, secret="MySecretSignedCookie")
        return redirect('/restricted')
    elif username == "user" and password == "pass":
        response.set_cookie('account', username, secret="MySecretSignedCookie")
        return redirect('/restricted')
    else:
        return redirect('/')


@get('/restricted')
def restricted():
    username = request.get_cookie('account', secret="MySecretSignedCookie")
    if username:
        return "Welcome {} to the restricted area".format(username)
    else:
        return "You are not authorized"


run(host="localhost", port=1234, reloader=True, debug=True)
