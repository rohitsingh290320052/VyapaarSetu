from fastapi import Request
from starlette.responses import Response

async def auth_middleware(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers['X-Powered-By'] = 'RetailLink'
    return response
