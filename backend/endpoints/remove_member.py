from aiohttp import web

from backend.utils.lock_utils import is_locked
from backend.utils.remove_data_utils import remove_members_data


async def remove_member(request: web.Request) -> web.Response:
    token = request.rel_url.query['token']

    # Checking if member is locked.
    if is_locked(token):
        return web.Response(
            status=200,
        )

    # Extracting inputs from frontend.
    group_name = request.rel_url.query['group_name']
    id_str = request.rel_url.query['id']
    id_ = int(id_str)
    remove_members_data(group_name, id_)
    return web.Response(status=200,
                        body="Member removed successfully.")