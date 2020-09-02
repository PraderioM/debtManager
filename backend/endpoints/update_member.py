from aiohttp import web

from backend.utils.lock_utils import is_locked
from backend.utils.modify_data_utils import modify_members_data
from backend.models.member import Member


async def update_member(request: web.Request) -> web.Response:
    token = request.rel_url.query['token']

    # Checking if member is locked.
    if is_locked(token):
        return web.Response(
            status=200,
        )

    # Extracting inputs from frontend.
    group_name = request.rel_url.query['group_name']
    fronted_data = Member.pre_process_request(request)
    id_str = request.rel_url.query['id']
    id_ = int(id_str)

    # Transforming member input from type "dict" to type "Member".
    member = Member.from_frontend(frontend_data=fronted_data)

    # Modifying member data.
    modify_members_data(member, id_, group_name)

    return web.Response(
        status=201,
        body="Member updated successfully."
    )
