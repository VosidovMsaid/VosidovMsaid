from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect
from numpy import outer

def index(request):
    return render(request,"firstapp/home.html")

def about(request):
    return render(request,"firstapp/about.html")

def contact(request):
    return render(request,"firstapp/contact.html")