# Fake Instagram

### Commands used in VSCode Terminal

##### Initial Setup

- cd ~/Desktop
- mkdir FakeInsta
- cd FakeInsta
- pip3 install pipenv
- pipenv install django
- pipenv shell
- django-admin startproject bookmarks .
- django-admin startapp account
- python manage.py migrate

##### Authentication

- python manage.py createsuperuser

##### User Models

- pip3 install Pillow
- python manage.py makemigrations
- python manage.py migrate

##### Social Authentication

- pip3 install social-auth-app-django
- python manage.py migrate

This will allow development server to run through HTTPS by using RunServerPlus which is django extension. To run it, you'll have to add https:// before the domain name

        - pip3 install django-extensions
        - pip3 install werkzeug
        - pip3 install pyOpenSSL

- python manage.py runserver_plus --cert-file cert.crt