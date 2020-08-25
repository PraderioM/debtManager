from aiohttp import web

from backend.utils.check_if_locked import check_if_locked
from backend.utils.add_data_utils import add_group_data
from backend.models.group import Group


async def add_group(request: web.Request) -> web.Response:
    data = await request.post()

    # Checking if member is locked.
    token = data["token"]
    if check_if_locked(token):
        return web.Response(
            status=200,
            body="Another person is using the app, sorry. You cannot modify stuff."
        )

    # Extracting inputs from frontend.
    database_data = [data["name"], data["mailgun_1"], data["mailgun_2"]]
    group = Group.from_database(database_data)

    # Adding flow inputs from frontend into database.
    add_group_data(group)
    return web.Response(
        status=201,
        body="Group added successfully."
    )