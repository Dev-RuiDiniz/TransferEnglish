from contextvars import ContextVar
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.responses import Response
from jose import jwt, JWTError
from app.core.config import settings

_tenant_id_context: ContextVar[str] = ContextVar("tenant_id", default="")

class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        # Skip tenant validation for public endpoints and OPTIONS preflight
        public_paths = ["/", "/api/v1/health", "/api/v1/login/access-token", "/api/v1/register"]
        if request.method == "OPTIONS" or request.url.path in public_paths:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.replace("Bearer ", "")
            try:
                payload = jwt.decode(
                    token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
                )
                tenant_id = payload.get("tenant_id")
                if tenant_id:
                    token = _tenant_id_context.set(tenant_id)
                    try:
                        response = await call_next(request)
                        return response
                    finally:
                        _tenant_id_context.reset(token)
            except JWTError:
                pass # Let the auth dependency handle the 403 error for better control

        return await call_next(request)

def get_current_tenant() -> str:
    return _tenant_id_context.get()
