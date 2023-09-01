from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, User
from .serializers import BookSerializer, PublicUserSerializer
import uuid


@api_view(["GET"])
def books(request):
    search = request.query_params.get("search", None)
    result = []
    if search is not None:
        result = Book.objects.filter(title__contains=search)
    else:
        result = Book.objects.all()
    result = BookSerializer(result, many=True)
    return Response(result.data, status=200)


@api_view(["GET"])
def users(request):
    users = User.objects.all()
    users = PublicUserSerializer(users, many=True)
    return Response(users.data, status=200)


@api_view(["POST"])
def borrow(request):
    book_id = request.data["book_id"]
    book = Book.objects.get(id=uuid.UUID(book_id))
    if book.borrower is not None:
        return Response("Book already borrowed", status=400)
    book.borrower = request.libuser.id
    book.save()
    return Response("Book borrowed", status=200)


@api_view(["POST"])
def return_book(request):
    book_id = request.data["book_id"]
    book = Book.objects.get(id=uuid.UUID(book_id))
    book.borrower = None
    book.save()
    return Response("Book returned", status=200)


@api_view(["GET"])
def user(request):
    retval = PublicUserSerializer(request.libuser).data
    print(retval)
    return Response(retval, status=200)
