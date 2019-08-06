---
output:
  html_document:
    keep_md: yes
    theme: cerulean
    highlight: tango
    code_folding: show
    toc: yes
    toc_float: yes
    number_sections: true
  pdf_document:
    number_sections: yes
geometry: margin = 1.2in
fontsize: 10pt
always_allow_html: yes
editor_options: 
  chunk_output_type: inline
---




# Getting started with Django 

## Why Django

Django is a Web framework written in Python. A Web framework is a software that supports the development of dynamic Web sites, applications, and services. It provides a set of tools and functionalities that solves many common problems associated with Web development, such as security features, database access, sessions, template processing, URL routing, internationalization, localization, and much more.

Using a Web framework, such as Django, enables us to develop secure and reliable Web applications very quickly in a standardized way, without having to reinvent the wheel.

## Installation

The first thing we need to do is install some programs on our machine so to be able to start playing with Django. The basic setup consists of installing Python, Virtualenv, and Django.

Using virtual environments is not mandatory, but it’s highly recommended. 

Assuming python is installed (using 3.7.2 currently), we are going to use pipenv, a tool to manage and install Python packages with even more features thant just using virtuenv


```bash
pip install pipenv
```

Once you’ve done that, you can effectively forget about pip since Pipenv essentially acts as a replacement. It also introduces two new files, the Pipfile (which is meant to replace requirements.txt) and the Pipfile.lock (which enables deterministic builds).

Pipenv uses pip and virtualenv under the hood but simplifies their usage with a single command line interface.


### Takes care of pinned dependencies


Pinning the flask dependency to a specific version ensures that a pip install -r requirements.txt sets up the exact version

With these pinned dependencies, you can ensure that the packages installed in your production environment match those in your development environment exactly, so your product doesn’t unexpectedly break.



pipenv shell --three

Creates Pipfile from reuqirements.txt

pipenv install

Install all packages



This will create a virtual environment if one doesn’t already exist. Pipenv creates all your virtual environments in a default location. 

Finally, here are some quick commands to find out where stuff is. How to find out where your virtual environment is:

$ pipenv --venv
How to find out where your project home is:

$ pipenv --where







Think of it like this: for each Django project you start, you will first create a Virtual Environment for it. It’s like having a sandbox for each Django project. So you can play around, install packages, uninstall packages without breaking anything.

## Installing Django >2.0

Activated the virtual environment, run the following command to install Django:


```bash
pip install django
```

## To start a New Project

To start a new Django project, run the command below:


```bash
django-admin startproject admin_proj
```

Django comes with a simple web server installed. It’s very convenient during the development, so we don’t have to install anything else to run the project locally. We can test it by executing the command:


```bash
python manage.py runserver
```


For now, you can ignore the migration errors; we will get to that later.

Now open the following URL in a Web browser: http://127.0.0.1:8000 and you should see the following page:

Picture

## Creating an App
        
In the Django philosophy we have two important concepts:

app: is a Web application that does something. An app usually is composed of a set of models (database tables), views, templates, tests.
project: is a collection of configurations and apps. One project can be composed of multiple apps, or a single app.


>django-admin startapp admin_app

This creates a folder structure for the app.



ow that we created our first app, let’s configure our project to use it.

To do that, open the settings.py and try to find the INSTALLED_APPS variable and include admin_app next to the 6 built-in apps

settings.py


```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'admin_app',
]
```

Source[^1]

# MVT

MVC vs MVTs

## Views

## Migrations

## Templates


### Plotly and Ajax scripts



```bash
sudo ls
```






***
[^1]: Adopted from https://hackernoon.com/dont-install-postgres-docker-pull-postgres-bee20e200198
