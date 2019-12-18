from django.shortcuts import render
from django.http import HttpResponse
#from .models import self

# Create your views here.

def print_intro(request,*args, **kwargs):
    return render(request,'home.htm',{})
    

def print_address(request,*args, **kwargs):
    return render(request,'address.htm',{})
