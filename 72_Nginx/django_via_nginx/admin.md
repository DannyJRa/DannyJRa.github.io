Source: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
mkdir django-on-docker && cd django-on-docker

mkdir app && cd app
pipenv install django==2.2.4
pipenv shell

django-admin.py startproject hello_django .
python manage.py migrate
python manage.py runserver





...

docker-compose build