from aiohttp import web

from src import logger
from src.views import routes

logger.init(__name__)
app = web.Application()
app.add_routes(routes)
