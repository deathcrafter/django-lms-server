from rest_framework import serializers
from .models import Book, User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "category", "borrower")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "email", "phone", "password", "address", "college")


class PublicUserSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField("get_books")

    def get_books(self, attrs):
        borrowed_books = Book.objects.filter(borrower=attrs.id)
        return BookSerializer(borrowed_books, many=True).data

    class Meta:
        model = User
        fields = ("id", "name", "email", "phone", "address", "college", "books")

    def validate(self, attrs):
        return super().validate(attrs)
