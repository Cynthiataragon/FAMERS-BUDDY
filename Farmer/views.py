from django import forms
from django.shortcuts import render, redirect
from Farmer.forms import FarmerForms
from Farmer.models import Farmer 
# Create your views here.
def frb(request):
    if request.method == "POST":
        form = FarmerForms(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/views')
                except:
                    pass
            else:
                form = FarmerForms()
            return render (request, 'index.html', {'form':forms})
