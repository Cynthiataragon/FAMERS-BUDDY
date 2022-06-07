from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello world I am working")

def signup(request):
    return render(request, "Template/signup.html")

def signin(request):
    return render(request, "Template/signin.html")

def signout(request):
    return render(request, "Template/signout.html")
    