from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Hello World</h1>") # string of HTML code

def otherpage_view(*args, **kwargs): # *args, **kwargs
    return HttpResponse("<h1>Hello Other Page</h1>") # string of HTML code