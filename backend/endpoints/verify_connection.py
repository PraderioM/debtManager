from aiohttp import web

from backend.utils.lock_utils import is_locked, update_lock


async def verify_connection(request: web.Request) -> web.Response:
    token = request.rel_url.query['token']

    # If database is locked we do nothing.
    if is_locked(token):
        return web.Response(status=200)

    # Otherwise we update the lock status.
    update_lock(token)

    return web.Response(status=201)
