from django.shortcuts import render
from .models import Lost
from datetime import datetime, timedelta

def index(request):
    
    all_lost = Lost.objects.all().order_by('date')

    lost_phone = all_lost.filter(title__contains = 'phone')

    lost_today = all_lost.filter(date = datetime.now())

    context = {'all_lost':all_lost, 'lost_phone':lost_phone, 'lost_today':lost_today}

    return render(request, 'landf/index.html', context)