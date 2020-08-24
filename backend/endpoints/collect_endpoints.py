from aiohttp import web

from .add_debt import add_debt
from .verify_connection import verify_connection


def collect_endpoints(app: web):
    app.router.add_get('/add-debt', add_debt)
    app.router.add_get('/verify-connection', verify_connection)
