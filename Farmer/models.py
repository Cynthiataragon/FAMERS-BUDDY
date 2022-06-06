import email
from django.forms import CharField, ModelForm, Textarea
from django.db import models

# Create your models here.
class Farmer(models.Model):
    id=models.CharField(max_length=20)
    f_name = models.CharField(max_length= 100)
    l_name = models.CharField(max_length=100)
    email= models.EmailField()
    password = models.CharField(max_length=10)