from aiohttp import web

from .add_flow import add_flow
from .verify_connection import verify_connection
from .get_token import get_token


def collect_endpoints(app: web):
    app.router.add_post('/add-debt', add_flow)
    app.router.add_post('/verify-connection', verify_connection)
    app.router.add_get('/get-token', get_token)
