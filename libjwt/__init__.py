from typing import Any
import jwt

secret = "my super secret key"  # This should be in an environment variable


def create_jwt(payload: dict[str, Any]):
    return jwt.encode(payload, secret, algorithm="HS256")


def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except jwt.InvalidTokenError:
        return None
