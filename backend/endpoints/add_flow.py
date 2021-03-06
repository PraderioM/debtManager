from datetime import date

from aiohttp import web

from backend.utils.lock_utils import is_locked
from backend.utils.add_data_utils import add_flow_data
from backend.models.flow import Flow


async def add_flow(request: web.Request) -> web.Response:
    data = await request.post()

    # Checking if member is locked.
    token = data["token"]
    if is_locked(token):
        return web.Response(
            status=200,
            body="Another person is using the app, sorry. You cannot modify stuff."
        )

    # Extracting inputs from frontend.
    group_name = request.rel_url.query['group_name']
    fronted_data = Flow.pre_process_request(request)

    # Transforming flow input from type "dict" to type "Flow".
    flow = Flow.from_frontend(frontend_data=fronted_data)

    # Adding flow inputs from frontend into database.
    add_flow_data(flow, group_name)
    return web.Response(
        status=201,
        body="Flow added successfully."
    )
