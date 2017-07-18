from aiohttp import web
import jinja2
import aiohttp_jinja2
import logging
from testforyou.db import init_connect, close_connect
from testforyou.router import setup_routes

logging.basicConfig(level=logging.INFO)

# create application
app = web.Application()

# setup routes
setup_routes(app)

# setup Jinja2 template render
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('testforyou', 'templates'))

app.on_startup.append(init_connect)
app.on_cleanup.append(close_connect)

# config static files
app.router.add_static('/static', 'static', name='static')

# run application
web.run_app(app, port=8080, host='localhost')
