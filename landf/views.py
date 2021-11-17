from django.shortcuts import render
from .models import Lost

def index(request):
    
    all_lost = Lost.objects.all()

    context = {'all_lost':all_lost}

    return render(request, 'landf/index.html', context)