import json

from aiohttp import web

from backend.utils.get_data_utils import get_members_data


async def get_member(request: web.Request) -> web.Response:
    group_name = request.rel_url.query['group_name']
    member_list = get_members_data(group_name)
    return web.Response(
        status=200,
        body=json.dumps([member.to_frontend() for member in member_list])
    )
