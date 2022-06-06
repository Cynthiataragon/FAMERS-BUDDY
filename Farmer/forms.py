from django import forms 
from Farmer.models import Farmer

class FarmerForms(forms.ModelForm):
    class Meta: 
        model = Farmer
        field = '_alt_'
    