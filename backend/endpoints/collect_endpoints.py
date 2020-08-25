from aiohttp import web

from backend.endpoints.add_flow import add_flow
from backend.endpoints.verify_connection import verify_connection
from backend.endpoints.get_token import get_token
from backend.endpoints.get_group_list import get_group_list


def collect_endpoints(app: web):
    app.router.add_post('/add-debt', add_flow)
    app.router.add_post('/verify-connection', verify_connection)

    app.router.add_get('/get-token', get_token)
    app.router.add_get('/get-group-list', get_group_list)
