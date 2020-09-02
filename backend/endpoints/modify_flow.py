from aiohttp import web

from backend.utils.lock_utils import is_locked
from backend.utils.modify_data_utils import modify_flow_data
from backend.models.flow import Flow


async def modify_flow(request: web.Request) -> web.Response:
    token = request.rel_url.query['token']

    # Checking if member is locked.
    if is_locked(token):
        return web.Response(
            status=200,
        )

    # Extracting inputs from frontend.
    group_name = request.rel_url.query['group_name']
    fronted_data = Flow.pre_process_request(request)
    id_str = request.rel_url.query['id']
    id_ = int(id_str)

    # Transforming flow input from type "dict" to type "Flow".
    flow = Flow.from_frontend(frontend_data=fronted_data)

    # Modifying flow data.
    modify_flow_data(flow, id_, group_name)

    return web.Response(
        status=201,
        body="Flow modified successfully."
    )
