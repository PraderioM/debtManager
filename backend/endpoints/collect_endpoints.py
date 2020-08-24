from aiohttp import web

from .add_debt import add_debt
from .verify_connection import verify_connection
from .get_token import get_token


def collect_endpoints(app: web):
    app.router.add_post('/add-debt', add_debt)
    app.router.add_post('/verify-connection', verify_connection)
    app.router.add_get('/get-token', get_token)
