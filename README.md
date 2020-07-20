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