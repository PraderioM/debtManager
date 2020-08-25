import json

from aiohttp import web

from backend.utils.get_data_utils import get_groups_data


async def get_group_list(request: web.Request) -> web.Response:
    group_list = get_groups_data()
    return web.Response(status=200, body=json.dumps([group.to_frontend() for group in group_list]))
