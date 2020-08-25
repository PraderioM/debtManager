import json
from aiohttp import web

from backend.utils.get_data_utils import get_periodic_flow_data


def get_periodic_flows_list(request: web.Request) -> web.Response:
    group_name = request.rel_url.query['group_name']
    periodic_flows_list = get_periodic_flow_data(group_name)
    return web.Response(status=200, body=json.dumps([periodic_flow.to_frontend() for periodic_flow in periodic_flows_list]))
