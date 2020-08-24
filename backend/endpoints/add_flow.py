from datetime import date
import csv

from aiohttp import web

from backend.utils.check_if_locked import check_if_locked
from backend.utils.get_data_utils import get_members_data
from backend.utils.add_data_utils import add_flow_data
from backend.models.flow import Flow


async def add_flow(request: web.Request) -> web.Response:
    data = await request.post()

    # Checking if member is locked.
    token = data["token"]
    if check_if_locked(token):
        return web.Response(
            status=200,
            body="Another person is using the app, sorry. You cannot modify stuff."
        )

    # Extracting inputs from frontend.
    database_data = [data["issuer"], data["receiver"], data["amount"], data["concept"], str(date.today())]
    flow = Flow.from_database(database_data, get_members_data(data['group_name']))

    # Adding flow inputs from frontend into database.
    add_flow_data(flow, data['group_name'])
    return web.Response(
        status=201,
        body="Flow added successfully."
    )