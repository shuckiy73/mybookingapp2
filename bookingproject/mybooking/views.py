import requests
from django.shortcuts import render, redirect

from .forms import SearchForm
from .models import SearchResult
from .serializers import SearchResultSerializer


def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data['location']
            checkin = form.cleaned_data['checkin']
            checkout = form.cleaned_data['checkout']
            guests = form.cleaned_data['guests']

            # Замените 'your_api_key' на ваш реальный API ключ
            api_key = 'https://hotels-comparer.com/2/?marker=553715'
            url = 'https://api.sutochno.ru'
            params = {
                'location': location,
                'checkin': checkin,
                'checkout': checkout,
                'guests': guests,
                'api_key': api_key
            }

            response = requests.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                search_result = SearchResult(
                    location=location,
                    checkin=checkin,
                    checkout=checkout,
                    guests=guests,
                    result_data=data
                )
                search_result.save()
                serializer = SearchResultSerializer(search_result)
                return render(request, 'search_results.html', {'results': serializer.data})
            else:
                return render(request, 'search_error.html', {'error': 'Failed to fetch data from API'})
    else:
        form = SearchForm()
    return render(request, 'search_form.html', {'form': form})


def search_view(request):
    if request.method == 'POST':
        # Здесь вы можете добавить логику для обработки данных формы
        location = request.POST.get('location')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        guests = request.POST.get('guests')

        # Пример запроса к API для получения результатов поиска
        api_url = f"https://api.example.com/search?location={location}&checkin={checkin}&checkout={checkout}&guests={guests}"
        response = requests.get(api_url)
        results = response.json()

        # Сохраняем результаты в сессии
        request.session['search_results'] = results

        # Перенаправляем на страницу с результатами
        return redirect('search_results')

    return render(request, 'search_form.html')


def results_view(request):
    # Получаем результаты из сессии
    results = request.session.get('search_results', {})
    return render(request, 'results.html', {'results': results})
