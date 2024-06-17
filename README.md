Создание полноценного приложения, аналогичного Суточно.ру или Booking.com, с использованием Django и Django Rest Framework (DRF) — это сложный и многоэтапный процесс. Ниже представлен обзор основных шагов и компонентов, которые потребуются для реализации такого приложения.

### 1. Настройка проекта Django

1. **Создание виртуального окружения:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте `venv\Scripts\activate`
   ```

2. **Установка Django и DRF:**
   ```bash
   pip install django djangorestframework
   ```

3. **Создание нового проекта Django:**
   ```bash
   django-admin startproject mybookingapp
   cd mybookingapp
   ```

4. **Создание приложения:**
   ```bash
   python manage.py startapp bookings
   ```

### 2. Настройка базы данных и моделей

1. **Определение моделей в `bookings/models.py`:**
   ```python
   from django.db import models
   from django.contrib.auth.models import User

   class Property(models.Model):
       name = models.CharField(max_length=255)
       description = models.TextField()
       price = models.DecimalField(max_digits=10, decimal_places=2)
       owner = models.ForeignKey(User, on_delete=models.CASCADE)

   class Booking(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       property = models.ForeignKey(Property, on_delete=models.CASCADE)
       start_date = models.DateField()
       end_date = models.DateField()
   ```

2. **Миграции:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 3. Настройка аутентификации

1. **Использование встроенной системы аутентификации Django:**
   ```python
   # mybookingapp/settings.py
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'rest_framework.authtoken',
       'bookings',
   ]

   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.TokenAuthentication',
       ],
   }
   ```

2. **Создание API для регистрации и аутентификации:**
   ```python
   # bookings/views.py
   from rest_framework.authtoken.models import Token
   from rest_framework.response import Response
   from rest_framework.views import APIView
   from .serializers import UserSerializer

   class RegisterView(APIView):
       def post(self, request):
           serializer = UserSerializer(data=request.data)
           if serializer.is_valid():
               user = serializer.save()
               token, created = Token.objects.get_or_create(user=user)
               return Response({'token': token.key})
           return Response(serializer.errors, status=400)
   ```

### 4. Создание API для бронирования и управления свойствами

1. **Сериализаторы:**
   ```python
   # bookings/serializers.py
   from rest_framework import serializers
   from django.contrib.auth.models import User
   from .models import Property, Booking

   class UserSerializer(serializers.ModelSerializer):
       class Meta:
           model = User
           fields = ('username', 'password')
           extra_kwargs = {'password': {'write_only': True}}

       def create(self, validated_data):
           user = User.objects.create_user(**validated_data)
           return user

   class PropertySerializer(serializers.ModelSerializer):
       class Meta:
           model = Property
           fields = '__all__'

   class BookingSerializer(serializers.ModelSerializer):
       class Meta:
           model = Booking
           fields = '__all__'
   ```

2. **Представления:**
   ```python
   # bookings/views.py
   from rest_framework import viewsets
   from .models import Property, Booking
   from .serializers import PropertySerializer, BookingSerializer

   class PropertyViewSet(viewsets.ModelViewSet):
       queryset = Property.objects.all()
       serializer_class = PropertySerializer

   class BookingViewSet(viewsets.ModelViewSet):
       queryset = Booking.objects.all()
       serializer_class = BookingSerializer
   ```

### 5. Настройка маршрутов

1. **Маршрутизация для API:**
   ```python
   # bookings/urls.py
   from django.urls import path, include
   from rest_framework.routers import DefaultRouter
   from .views import PropertyViewSet, BookingViewSet, RegisterView

   router = DefaultRouter()
   router.register(r'properties', PropertyViewSet)
   router.register(r'bookings', BookingViewSet)

   urlpatterns = [
       path('register/', RegisterView.as_view(), name='register'),
       path('', include(router.urls)),
   ]
   ```

2. **Включение маршрутов в основной проект:**
   ```python
   # mybookingapp/urls.py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('api/', include('bookings.urls')),
   ]
   ```

### 6. Дополнительные функции

1. **Фильтрация и поиск:**
   ```python
   # bookings/views.py
   from rest_framework import filters

   class PropertyViewSet(viewsets.ModelViewSet):
       queryset = Property.objects.all()
       serializer_class = PropertySerializer
       filter_backends = [filters.SearchFilter]
       search_fields = ['name', 'description']
   ```

2. **Управление пользователями:**
   ```python
   # bookings/views.py
   from rest_framework import permissions

   class UserViewSet(viewsets.ModelViewSet):
       queryset = User.objects.all()
       serializer_class = UserSerializer
       permission_classes = [permissions.IsAdminUser]
   ```

### 7. Тестирование и развертывание

1. **Тестирование API:**
   ```bash
   python manage.py test
   ```

2. **Развертывание на сервере:**
   - Настройка сервера (например, Nginx, Gunicorn).
   - Настройка базы данных и статических файлов.
   - Запуск приложения.

Этот обзор охватывает основные шаги для создания полноценного приложения с аутентификацией, бронированием, фильтрацией, поиском и управлением пользователями на Django и DRF. Для полной реализации потребуется более детальная проработка каждого компонента и возможно интеграция дополнительных сервисов и функций.

### 1. Установка и настройка Bootstrap

1. **Скачайте Bootstrap:**
   Вы можете скачать Bootstrap с официального сайта или использовать CDN для подключения стилей и скриптов.

2. **Подключение через CDN:**
   Добавьте следующие строки в ваш HTML-файл для подключения Bootstrap:
   ```html
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
   ```

### 2. Создание базового шаблона HTML

1. **Создайте папку `templates` в корне вашего проекта:**
   ```bash
   mkdir mybookingapp/templates
   ```

2. **Создайте файл `base.html` в папке `templates`:**
   ```html
   <!-- mybookingapp/templates/base.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>My Booking App</title>
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
   </head>
   <body>
       <nav class="navbar navbar-expand-lg navbar-light bg-light">
           <div class="container-fluid">
               <a class="navbar-brand" href="#">My Booking App</a>
               <div class="collapse navbar-collapse">
                   <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                       <li class="nav-item">
                           <a class="nav-link" href="#">Home</a>
                       </li>
                       <li class="nav-item">
                           <a class="nav-link" href="#">Properties</a>
                       </li>
                       <li class="nav-item">
                           <a class="nav-link" href="#">Bookings</a>
                       </li>
                   </ul>
               </div>
           </div>
       </nav>
       <div class="container mt-5">
           {% block content %}
           {% endblock %}
       </div>
       <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
   </body>
   </html>
   ```

### 3. Создание `index.html`

1. **Создайте файл `index.html` в папке `templates`:**
   ```html
   <!-- mybookingapp/templates/index.html -->
   {% extends 'base.html' %}

   {% block content %}
   <h1>Welcome to My Booking App</h1>
   <p>Find and book your perfect property!</p>
   {% endblock %}
   ```

### 4. Настройка Django для использования шаблонов

1. **Обновите настройки Django для использования папки `templates`:**
   ```python
   # mybookingapp/settings.py
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [BASE_DIR / 'templates'],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

### 5. Создание представления для `index.html`

1. **Создайте представление в `views.py`:**
   ```python
   # mybookingapp/views.py
   from django.shortcuts import render

   def index(request):
       return render(request, 'index.html')
   ```

2. **Добавьте маршрут в `urls.py`:**
   ```python
   # mybookingapp/urls.py
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
       # другие маршруты
   ]
   ```

### 6. Добавление собственных стилей CSS

1. **Создайте папку `static` в корне вашего проекта:**
   ```bash
   mkdir mybookingapp/static
   ```

2. **Создайте файл `style.css` в папке `static`:**
   ```css
   /* mybookingapp/static/style.css */
   body {
       background-color: #f8f9fa;
   }
   ```

3. **Подключите CSS-файл в `base.html`:**
   ```html
   <!-- mybookingapp/templates/base.html -->
   <head>
       <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
       <link href="{% static 'style.css' %}" rel="stylesheet">
   </head>
   ```

Теперь у вас есть базовый шаблон HTML, стилизованный с помощью Bootstrap, и собственный CSS-файл для дополнительных настроек. Вы можете расширять и модифицировать эти файлы в соответствии с требованиями вашего проекта.

### `base.html`

```html
<!-- mybookingapp/templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Booking App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="{% static 'style.css' %}" rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">My Booking App</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Properties</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Bookings</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <div class="container mt-5">
        <form class="row g-3 mb-5" method="GET" action="{% url 'search' %}">
            <div class="col-md-4">
                <label for="location" class="form-label">Курорт, город или адрес</label>
                <input type="text" class="form-control" id="location" name="location" list="locationOptions">
                <datalist id="locationOptions">
                    <option value="Санкт-Петербург">
                    <option value="Москва">
                    <option value="Сочи">
                    <option value="Минск">
                    <option value="Казань">
                    <option value="Дагестан">
                    <option value="Кисловодск">
                    <option value="Абхазия">
                </datalist>
            </div>
            <div class="col-md-2">
                <label for="checkin" class="form-label">Заезд</label>
                <input type="date" class="form-control" id="checkin" name="checkin">
            </div>
            <div class="col-md-2">
                <label for="checkout" class="form-label">Отъезд</label>
                <input type="date" class="form-control" id="checkout" name="checkout">
            </div>
            <div class="col-md-2">
                <label for="guests" class="form-label">Гости</label>
                <select class="form-select" id="guests" name="guests">
                    <option selected>2 взрослых, без детей</option>
                    <!-- Другие варианты -->
                </select>
            </div>
            <div class="col-md-2">
                <button type="submit" class="btn btn-primary mt-4">Поиск</button>
            </div>
        </form>
        {% block content %}
        {% endblock %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

### `index.html`

```html
<!-- mybookingapp/templates/index.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Welcome to My Booking App</h1>
<p>Find and book your perfect property!</p>
{% endblock %}
```

### `search_results.html`

```html
<!-- mybookingapp/templates/search_results.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Результаты поиска</h1>
<ul>
    {% for result in results %}
    <li>{{ result }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

### `views.py`

```python
# mybookingapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        checkin = request.GET.get('checkin')
        checkout = request.GET.get('checkout')
        guests = request.GET.get('guests')
        # Здесь вы можете добавить логику для поиска по вашей базе данных
        results = []  # Замените на реальные результаты поиска
        return render(request, 'search_results.html', {'results': results})
```

### `urls.py`

```python
# mybookingapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    # другие маршруты
]
```

### `settings.py`

```python
# mybookingapp/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Этот код включает в себя все необходимые изменения для добавления формы поиска на вашу HTML-страницу, обработки данных формы и отображения результатов поиска.
