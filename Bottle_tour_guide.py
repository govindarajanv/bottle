from bottle import route, run, request, response, redirect


@route('/', method=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return '''
       <form action="/" method="post" enctype="multipart/form-data">
          Username: <input type="text" name="user"/>
          Password: <input type="password" name="password"/>
          <input type="submit" value="Login" />
        </form>
       '''
    else:
        if request.forms.get('user') == 'admin' and request.forms.get('password') == 'pass':
            response.set_cookie('user', request.forms.get('user'))
            return redirect('/welcome')
        elif request.forms.get('user') == 'user' and request.forms.get('password') == 'password':
            response.set_cookie('user', request.forms.get('user'))
            return redirect('/welcome')
        response.set_cookie('user', 'guest')
        return redirect('/welcome')


# http://localhost:1234
@route('/welcome')
def welcome():
    if request.get_cookie('visited'):
        if request.get_cookie('user') == "admin":
            return "welcome back, Admin"
        elif request.get_cookie('user') == "guest":
            return "Welcome Guest to the site"
        else:
            return "Welcome back to the site"
        response.delete_cookie('user')
    else:
        response.set_cookie('visited', 'yes')
        return "Welcome Guest!. You have visited for the first time"


run(host="localhost", port=1234, debug=True)
