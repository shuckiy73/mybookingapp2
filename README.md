

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
