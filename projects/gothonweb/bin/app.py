import web
from gothonweb.map import *

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
    # '/show_room', 'show_room',
    # '/hello', 'hello_form'
)

app = web.application(urls, locals())

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'room': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = START
        web.seeother("/game")


class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room)
        else:
            # why is this here? do you need to do it?
            return render.you_died()

    def POST(self):
        form = web.input(action=None)

        # there is a bug here, can you fix it?
        if session.room and form.action:
            session.room = session.room.go(form.action)

        web.seeother("/game")


if __name__ == '__main__':
    app.run()
