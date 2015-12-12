import bottle

@bottle.route('/')
def index():
    return '<b>Hola</b>'


bottle.run(host='127.0.0.1', port=8080)
