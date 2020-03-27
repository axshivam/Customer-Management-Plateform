from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is the main page")

def product(request):
    return HttpResponse("This is the product page")

def customer(request):
    return HttpResponse("This is the customer page")
