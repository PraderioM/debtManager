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
        )

    # Extracting inputs from frontend.
    database_data = [request.rel_url.query[val] for val in ["name", "mailgun_1", "mailgun_2"]]
    group = Group.from_database(database_data)

    # Adding flow inputs from frontend into database.
    add_group_data(group)
    return web.Response(
        status=201,
    )
