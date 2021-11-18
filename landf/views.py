from django.shortcuts import get_object_or_404, render
from .models import Lost
from datetime import datetime, timedelta

def index(request):
    
    all_lost = Lost.objects.all().order_by('date')

    lost_phone = all_lost.filter(title__contains = 'phone')

    lost_today = all_lost.filter(date = datetime.now())

    context = {'all_lost':all_lost, 'lost_phone':lost_phone, 'lost_today':lost_today}

    return render(request, 'landf/index.html', context)

def detail(request, lost_id):

    lost = get_object_or_404(Lost, pk=lost_id)

    context = {'lost': lost}

    return render(request, 'landf\detail.html', context)

def search(request):

    all_lost = Lost.objects.all().order_by('date')

    if len(request.GET) == 0:
        relevant_events = all_lost
    else:
        search_string = request.GET['q']
        relevant_lost = all_lost.filter(title__contains = search_string)
    context = {'relevant_lost': relevant_lost}

    return render(request, 'landf/search.html', context)