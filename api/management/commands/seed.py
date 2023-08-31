from django.core.management.base import BaseCommand, CommandError
from api.models import Book


class Command(BaseCommand):
    help = "Seeds the database with some books"

    def handle(self, *args, **options):
        if Book.objects.count() > 0:
            self.stdout.write(
                self.style.WARNING("Books already present in the database")
            )
            return
        book1 = Book(title="The Lost World", category="Sci-fi")
        book1.save()
        book2 = Book(title="Dune", category="Sci-fi")
        book2.save()
        book3 = Book(title="Alchemist", category="Fiction")
        book3.save()
        book4 = Book(title="Dune", category="Fiction")
        book4.save()
        book5 = Book(title="Champak", category="Comedy")
        book5.save()
        book6 = Book(title="Tenaliraman", category="Comedy")
        book6.save()

        self.stdout.write(self.style.SUCCESS("Seeded the database with some books"))


# Run this file with the following command:
# python manage.py seed
