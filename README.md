# Django-P2G3-mahya-smnt

## 1- create venv
```bash
python -m venv .venv
source .venv/Scripts/activate
pip install Django
```

## 2- create a django project
```bash
django-admin startproject config .
```

## 3- start project
```bash
python manage.py runserver
```

## 4- create an app with name blog
```bash
python manage.py startapp blog
```

- add 'blog' installed app in setting.py
- create file urls.py, and add it to urls.py in core/config
```
path('', inlcude('blog.urls'))
```
- add new view in views.py in blog
```
from django.http import HttpResponse
def about_us(request):
    return HttpResponse('this is a about us')
```

- add path to urls.py in blog
```
from django.urls import path
from . import views

urlpatterns = [
    path('about-us/', views.about_us),
    path('contact-us/', views.contact_us),
]
```


## 5- Define a path for render HTML
Create a index.html -> (root + blog/templates/blog/index.html)
Create a base.html ->  (root + templates/base.html) fill with basic html code

in index.html 
```html
{% extends 'base.html' %}
```
- add partitions (navbar, footer, sidebar)
create a navabr.html -> (root + templates/includes)
in base.html add follwing code
```html
{% include "includes/navbar.html" %}
```

- add block
for specific places, set a block with name in base.html
```html
{% block content %}{% endblock content %}
```

add index.html add following code
```html

{% block content %}
    <h1>
        Home page
    </h1>
{% endblock content %}
```
## 6- Add table
add tabel field in models.py
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()
    
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- run command to makemigrations and migrate

```bash
python manage.py makemigrations
python manage.py migrate

```

7- show tables in admin panel
create a super user
```python
python manage.py createsuperuser 
user: admin
email: admin@admin.com
password: admin
```
- add Product table to admin.py
```python
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', "name", "price", "stock"]
    
admin.site.register(Product, ProductAdmin)
```
