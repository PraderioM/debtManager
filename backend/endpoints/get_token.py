from aiohttp import web
from uuid import uuid4


async def get_token(request: web.Request) -> web.Response:
    return web.Response(status=200, body=str(uuid4()))
