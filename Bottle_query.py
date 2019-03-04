from bottle import route, run, template, request


# http://localhost:1234/wikipage?pageid=1&section=3
@route('/wikipage')
def wiki_page():
    pageid = request.query.pageid or "0"
    section = request.query.section or "0"

    return template("The requested wiki page with pageid {{pageid}} and section id {{sectionid}}", pageid=pageid,
                    sectionid=section)


run(host="localhost", port=1234, debug=True)
