from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Book, User
from api.serializers import PublicUserSerializer, UserSerializer
import libjwt

# Create your views here.


@api_view(["POST"])
def login(request):
    username = request.data["username"]
    password = request.data["password"]
    user = User.objects.get(email=username, password=password) or User.objects.get(
        phone=username, password=password
    )

    if user is None:
        return Response("User not found", status=404)

    token = libjwt.create_jwt({"user_id": str(user.id)})
    pub_user = PublicUserSerializer(user).data

    return Response({"token": token, "user": pub_user}, status=200)


@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User created", status=201)
    return Response(serializer.errors, status=400)
