from aiohttp import web


async def verify_connection(request: web.Request):
    post_data = await request.post()
    token = post_data['token']
    pass
