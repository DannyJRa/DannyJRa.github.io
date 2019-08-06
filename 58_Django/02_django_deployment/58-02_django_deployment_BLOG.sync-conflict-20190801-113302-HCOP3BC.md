---
title: Pipenv 
author: DannyJRa
date: '2019-01-25'
slug: 19_pipenv3
categories:
  - Python
tags:
  - Engineering
hidden: false
image: "img/19_pipenv_BLOG.gif"
share: false
output:
  html_document:
    keep_md: yes
    includes:
      #before_body: header.html
      #after_body: footer.html
    theme: cerulean
    highlight: tango
    code_folding: show
    toc: yes
    toc_float: yes
  pdf_document:
    number_sections: yes
geometry: margin = 1.2in
fontsize: 10pt
always_allow_html: yes

---

# Why Django
Django is a lifesaver if you want to create a CRUD app with batteries included without getting sidetracked.

> Django - so much developer convenience

The Web framework for perfectionists with deadlines

Django makes it very easy and fun to build a certain type of web application - a CRUD (create, read, update, delete) app.
Almost every single real-world web app can be started as a simple CRUD app.
With Django, you won’t have to reinvent the wheel. It just works and lets you focus on your business logic and creating something users can use.
Most things you will probably need already exist, and don’t need to be plugged together e.g. things like auth, user accounts, data migrations and the amazing admin interface.
It brings along a lot of convenience. If you were to use a micro framework instead of Django, you’ll end up reinventing or stitching together things you “wish you had in place already” like:

* ORM
* Migrations!
* Forms
* User management
* An easy way to add REST
* Lots of choices you don’t know you need have been made for you
* Lots and lots of structure and boilerplate
* Easy access to plugins
* An amazing amount of dev tooling

Sometimes, I’ll reach for Flask to get started with a simple prototype. But in the end, Django is my most productive tool for building classical sites which will be easy to maintain.
However, there are things which Django just wasn’t designed for. Things you CAN use it for, but you’ll feel like you’re doing things wrong and fighting an uphill battle.

BUT, if you really need to keep things minimalistic and want to avoid implicit choices, Django’s magic will get into your way. If you don’t want to use a relational database, you’re in for trouble. Doing lots of things in a parallelized fashion is not really straightforward. This is where Go shines!

Aus <https://vsupalov.com/go-and-django/>

# Adding vue.js
One additional mention: VueJS. I LOVE it for the convenience of putting together an easy dynamic interface, no matter what backend language I work in. No REST endpoints are needed, but you can transition to them eventually. There’s almost no setup overhead - just a single .html file. If you haven’t got a convenient way to whip up a quick fancy UI for your web app projects, you should check it out!
    Aus <https://vsupalov.com/go-and-django/>
## Vue.js In A Django Template
Aus <https://vsupalov.com/vue-js-in-django-template/>

# Django in Production
## Gunicorn and Nginx in a nutshell
    Aus <https://vsupalov.com/gunicorn-and-nginx/>

# Very interesting Django Packages in 2019[^1]
I tried to limit this overview to packages, which will be useful for any project, and you should know about. They do one thing, do it well, and don’t require you to change your whole project to suit them.
Debugging in Dev and Prod

* django-debug-toolbar - adds a toolbar on the right side of your Django page while in development. The toolbar shows lots of useful debug information!
* sentry - I love Sentry so much. It’s a SaaS which can notify you when your Django project crashes or errors out. It shows lots of useful details and is very pleasant to use.
• django-extensions - a collection of custom extensions for Django. There’s a lot in there! I’ll limit myself to the most important two tools: runserver_plusgives you the possibility to look into your app at any time. shell_plus --notebook lets you open a friggin jupyter notebook and prototype in it.
User Management
• django-allauth - add social login to your site, and extend the way people can register. A must-have if you want to have users with social auth.
Views and Forms
• django-braces - helpful mixins for Django’s class-based views.
• django-crispy-forms - control the rendering behaviour of forms with the {% crispy %} tag.
• django-bleach - advanced input cleaning.
• django-autocomplete-light - add autocompletion to your forms.
• django-shapeshifeter - handle multiple forms in a single view. Useful when your CRUD app starts shifting towards workflow-focused interfaces.
• django-extra-views - more class-based views, which can come in handy.
Frontend & APIs
• django-webpack-loader - include bundles built with webpack into your templates. Really useful if you have non-trivial JS in your project.
• django-pipeline - an asset packaging library for Django. No Webpack in sight, which can feel like a blessing sometimes. I myself prefer using Webpack these days, but this is a valid option as well.
• Django REST framework (DRF) - build RESTful APIs. It’s really good!
• graphene-django - build a GraphQL endpoint for your project. REST is fine, but frontend devs love to have a single GQL endpoint. They are very convenient.
• django-cors-headers - handle CORS (cross origin resource sharing) by including the right headers. Useful if your backend is on another domain than your frontend.
Data-Related Functionality
• django-taggit - add tags to any of your models! It’s simple to use, and fits well into most projects.
• django-filter - let users filter a list of objects themselves through a form.
• django-tables2 - display your data in nifty tables outside of the admin interface (works with django-filter).
• django-sql-explorer - write SQL queries on your Django-owned data and see results in a nice interface. A quick way to get going with reporting.
• djangoql - add a more advanced query language to the admin. This can be a nice compromise before investing more into BI tools or writing custom scripts.
• django-import-export - get data in and out of your app using CSV, JSON and other formats. Exactly what it sounds like and very handy.
Want more?
A good way to find cool tech, is to look at successful and popular open source projects related to Django. They know what’s good and include those techniques and packages into the code if it’s possible. You can find projects by looking at GitHub.
You can also browse through Django Packages where you can find a complete list of all packages out there and projects written in Django! Django Sites is another cool site, listing Django pages which provide their source code.
You can also learn a lot, from looking into popular starter templates. For example, check out cookiecutter-django and see a few of the above packages in action.

Aus <https://vsupalov.com/favorite-django-packages-2019/>


[^1] From <https://vsupalov.com/favorite-django-packages-2019/>
