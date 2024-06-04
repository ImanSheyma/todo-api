from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy
from ..config import SECRET, LIFETIME

cookie_transport = CookieTransport(cookie_name='todos', cookie_max_age=LIFETIME)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=LIFETIME)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)