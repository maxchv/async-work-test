import aiomysql


async def init_connect(app):
    # FIXME: get config to connect db
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='',
                                  db='testforyou', loop=app.loop)
    app['conn'] = conn


async def close_connect(app):
    app['conn'].close()
