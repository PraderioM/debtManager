from aiohttp import web
from .verify_connection import verify_connection
from .check_if_locked import check_if_locked
import csv


async def add_flow(request: web.Request) -> web.Response:
    # Checking if member is locked.
    data = await request.post()
    token = data["token"]
    if check_if_locked(token):
        return web.Response(
            status=200,
            body="Another person is using the app, sorry. You cannot modify stuff."
        )
    issuer = data["issuer"]
    receiver = data["receiver"]
    amount = data["amount"]
    concept = data["concept"]
    date = data["date"]

    # Adding




    # meter everything en csv
    # return a frontend, status 200
