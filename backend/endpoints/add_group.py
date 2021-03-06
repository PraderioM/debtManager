from aiohttp import web

from backend.utils.lock_utils import is_locked
from backend.utils.add_data_utils import add_group_data
from backend.models.group import Group


async def add_group(request: web.Request) -> web.Response:
    token = request.rel_url.query['token']

    # Checking if member is locked.
    if is_locked(token):
        return web.Response(
            status=200,
            body="Another person is using the app, sorry. You cannot modify stuff."
        )

    # Extracting inputs from frontend.
    frontend_data = Group.pre_process_request(request)

    # Transforming group input from type "dict" to type "Group".
    group = Group.from_frontend(frontend_data=frontend_data)

    # Adding group inputs from frontend into database.
    add_group_data(group)
    return web.Response(
        status=201,
        body="Group added successfully."
    )
