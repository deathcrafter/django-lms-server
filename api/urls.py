from django.urls import path
from .views import *

protected_urls = [
    "/api/borrow",
    "/api/return",
    "/api/user",
]

urlpatterns = [
    path("books", books),
    path("users", users),
    path("borrow", borrow),
    path("return", return_book),
    path("user", user),
]
