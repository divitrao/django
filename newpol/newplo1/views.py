from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import  news_for_admin

# Create your views here.

def index(request):
    content = news_for_admin.objects.all()
    return render(request, 'index.html', {'content': content})
