import json

from aiohttp import web

from backend.utils.get_data_utils import get_flow_data


async def get_flows(request: web.Request) -> web.Response:
    group_name = request.rel_url.query['group_name']
    flow_list = get_flow_data(group_name)
    return web.Response(
        status=200,
        body=json.dumps([flow.to_frontend() for flow in flow_list])
    )
