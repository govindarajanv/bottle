from bottle import run, route


# http://localhost:1234/forum/foo
# two declarators are required
@route('/forum')
@route('/forum/<name>')
def forum(name='default'):
    return "You have visited the forum: {} ".format(name)


@route('/<action>/<username>')
def manager(action, username):
    return "You have specified action: {} on username :{} ".format(action, username)


run(host="localhost", port=1234, debug=True)
