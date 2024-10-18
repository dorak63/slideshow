from django.shortcuts import render
from .models import SlideShow

def home(request):
    return render(request,  'SlideShow/home.html')
