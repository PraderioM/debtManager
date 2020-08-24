from aiohttp import web

from .add_debt import add_debt


def collect_endpoints(app: web):
    app.router.add_get('/add-debt', add_debt)
