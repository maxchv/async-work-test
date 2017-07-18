import aiohttp_jinja2
import logging

from testforyou.models import Course

logger = logging.getLogger(__name__)


@aiohttp_jinja2.template("courses/index.html")
async def index(request):
    courses = []
    async with request.app['conn'].cursor() as cursor:
        await cursor.callproc('select_courses')
        _all = await cursor.fetchall()
        courses = [Course(*c) for c in _all]
    return {'courses': courses}
