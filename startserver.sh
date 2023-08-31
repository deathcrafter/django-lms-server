# install dependencies
pip install -q -r requirements.txt

# create the database
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate api

# create superuser
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_PASSWORD=admin@123
export DJANGO_SUPERUSER_EMAIL=admin@example.com
python manage.py createsuperuser --noinput

# seed data
python manage.py seed

# start server
python manage.py runserver