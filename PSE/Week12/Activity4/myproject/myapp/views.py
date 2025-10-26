from django.shortcuts import render

from django.http import HttpResponse

def welcome(request, name):
    """
    A simple Django view that takes a name from the URL
    and returns a personalized welcome message.
    """
    return HttpResponse(f"<h1>Welcome {name.capitalize()} to Django!</h1>")

def index(request):
    return HttpResponse("<h1>Welcome Home</h1><p>Try <a href='/welcome/Salim/'>/welcome/Salim/</a></p>")