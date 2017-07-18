import aiohttp_jinja2 as aiohttp_jinja2

from .views import index


def setup_routes(app):
    app.router.add_get("/", index)

