import asyncio
import os

from aiohttp import web
import aiohttp_cors

from .endpoints.collect_endpoints import collect_endpoints
from .check_messages_to_send import check_messages_to_send
from .check_periodic_debts import check_periodic_debts


async def create_app():  # Start the app
    app_ = web.Application()

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app_, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Register handlers.
    collect_endpoints(app)

    # Configure CORS on all routes (deactivate it).
    for route in list(app_.router.routes()):
        cors.add(route)

    return app_


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(create_app())
    loop.run_forever(check_periodic_debts())
    loop.run_forever(check_messages_to_send())
    web.run_app(app, host=os.environ.get('HOST', '0.0.0.0'), port=os.environ.get('PORT', 2121))
