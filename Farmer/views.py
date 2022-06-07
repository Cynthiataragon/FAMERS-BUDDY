from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, "Template/index.html")

def signup(request):
    return render(request, "Template/signup.html")

def signin(request):
    return render(request, "Template/signin.html")

def signout(request):
    pass
    