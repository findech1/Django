from django.shortcuts import render

# Create your views here.
# myapp/views.py

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World this is my first django project!")
def contact(request):
    return HttpResponse("Contact page")

