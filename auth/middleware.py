import uuid
from api.models import User
from libjwt import decode_jwt
from rest_framework.response import Response
from api.urls import protected_urls


class JWTMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path not in protected_urls:
            print("Not protected")
            return None

        token = request.headers.get("Authorization", None)
        if token is not None and token.startswith("Bearer "):
            token = token.split(" ")[1]
            payload = decode_jwt(token)
            if payload is not None:
                request.libuser = User.objects.get(id=uuid.UUID(payload["user_id"]))
                if request.libuser is not None:
                    return None

        return Response("Unauthorized", status=401)
