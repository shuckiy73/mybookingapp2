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
