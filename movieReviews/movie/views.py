import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Create your views here.

def home(request):
    searchterm = request.GET.get("searchMovie")
    movies = Movie.objects.all() 
    return render(request, 'home.html', {"searchterm":searchterm, 'movies': movies})


def about(request):
    return HttpResponse('<h1>Welcome to About page<\h1>')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})