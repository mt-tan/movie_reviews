from curses.ascii import HT
import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Welcome to Home page<\h1>')


def about(request):
    return HttpResponse('<h1>Welcome to About page<\h1>')