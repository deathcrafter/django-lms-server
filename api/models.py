from django.db import models
from uuid import uuid4


# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    borrower = models.UUIDField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=400)
    college = models.CharField(max_length=100)

    def __str__(self):
        return self.name
