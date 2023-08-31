from .models import Book


def seed():
    if Book.objects.count() > 0:
        print("Books already present in the database")
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

    print("Seeded the database with some books")


# Run this file with the following command:
# python manage.py shell < api/seed.py

# You can also run this file from the Django shell:
# python manage.py shell
# >>> exec(open('api/seed.py').read())
