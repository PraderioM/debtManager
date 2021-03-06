from aiohttp import web

from backend.utils.lock_utils import is_locked
from backend.utils.add_data_utils import add_member_data
from backend.models.member import Member


async def add_member(request: web.Request) -> web.Response:
    token = request.rel_url.query['token']

    # Checking if member is locked.
    if is_locked(token):
        return web.Response(
            status=200,
            body="Another person is using the app, sorry. You cannot modify stuff."
        )

    # Extracting inputs from frontend.
    group_name = request.rel_url.query['group_name']
    fronted_data = Member.pre_process_request(request)

    # Transforming member input from type "dict" to type "Member".
    member = Member.from_frontend(frontend_data=fronted_data)

    # Adding inputs from frontend into database.
    add_member_data(member, group_name)
    return web.Response(
        status=201,
        body="Member added successfully."
    )
