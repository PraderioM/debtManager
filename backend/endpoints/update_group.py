from aiohttp import web

from backend.utils.lock_utils import is_locked
from backend.utils.modify_data_utils import modify_group_data
from backend.models.group import Group


async def update_group(request: web.Request) -> web.Response:
    token = request.rel_url.query['token']

    # Checking if member is locked.
    if is_locked(token):
        return web.Response(
            status=200,
        )

    # Extracting inputs from frontend.
    fronted_data = Group.pre_process_request(request)
    id_str = request.rel_url.query['id']
    id_ = int(id_str)

    # Transforming group input from type "dict" to type "Group".
    group = Group.from_frontend(frontend_data=fronted_data)

    # Modifying member data.
    modify_group_data(group, id_)

    return web.Response(
        status=201,
        body="Group updated successfully."
    )
