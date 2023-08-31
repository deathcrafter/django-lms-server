@REM install dependencies
pip install -q -r requirements.txt

@REM create the database
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate api

@REM create a superuser
SET DJANGO_SUPERUSER_USERNAME=admin
SET DJANGO_SUPERUSER_PASSWORD=admin@123
SET DJANGO_SUPERUSER_EMAIL=admin@example.com
python manage.py createsuperuser --email admin@example.com --username admin --noinput

@REM seed the database
python manage.py seed

@REM start the server
python manage.py runserver
