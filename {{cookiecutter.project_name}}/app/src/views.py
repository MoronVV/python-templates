import logging

from aiohttp import web

logger = logging.getLogger(__name__)
routes = web.RouteTableDef()


@routes.get('/')
def index(request):
    logger.debug("I'm a teapot")
    return web.Response(text="I'm a teapot", status=418)
