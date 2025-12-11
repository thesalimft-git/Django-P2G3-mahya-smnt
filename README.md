# Django-P2G3-mahya-smnt

1- create venv
```bash
python -m venv .venv
source .venv/Scripts/activate
pip install Django
```

2- create a django project
```bash
django-admin startproject config .
```

3- start project
```bash
python manage.py runserver
```

4- create an app with name blog
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


5- define a path for request/reponse