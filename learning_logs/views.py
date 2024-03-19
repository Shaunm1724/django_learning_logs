from django.shortcuts import render, HttpResponse
from .models import *

def home(request):
    return render(request, 'home.html')

def user(request):
    items = UserProfile.objects.all()
    return render(request, 'user.html', {'users': items})

def topic(request):
    items = Topic.objects.all()
    return render(request, 'topic.html', {'topics': items})

def entry(request):
    return HttpResponse("Make an entry")