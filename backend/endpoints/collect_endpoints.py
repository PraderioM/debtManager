from aiohttp import web

from backend.endpoints.add_flow import add_flow
from backend.endpoints.add_group import add_group
from backend.endpoints.verify_connection import verify_connection
from backend.endpoints.get_token import get_token
from backend.endpoints.get_summary import get_summary
from backend.endpoints.get_periodic_flows import get_periodic_flows_list
from backend.endpoints.get_flows import get_flow_list
from backend.endpoints.get_members import get_member_list
from backend.endpoints.get_group_list import get_group_list


def collect_endpoints(app: web):
    app.router.add_post('/add-group', add_group)
    app.router.add_post('/add-flow', add_flow)
    app.router.add_post('/verify-connection', verify_connection)

    app.router.add_get('/get-token', get_token)
    app.router.add_get('/get-summary', get_summary)
    app.router.add_get('/get-periodic-flows', get_periodic_flows_list)
    app.router.add_get('/get-flows', get_flow_list)
    app.router.add_get('/get-members', get_member_list)
    app.router.add_get('/get-group-list', get_group_list)
