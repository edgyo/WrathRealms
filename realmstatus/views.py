from django.http import HttpResponse
from django.shortcuts import render
from .models import Realm

# Create your views here.
def info(request):
    return render(request, 'info.html')

def america(request):
    return render(request, 'america.html')

def europe(request):
    return render(request, 'europe.html')

def russia(request):
    return render(request, 'russia.html')

def index(request):
    realms = Realm.objects.order_by('name')
    output = ', '.join([r.name for r in realms])
    return render(request,'index.html')