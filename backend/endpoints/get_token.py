from aiohttp import web
import json
from uuid import uuid4


async def get_token(request: web.Request) -> web.Response:
    return web.Response(status=200, body=json.dumps(str(uuid4())))
