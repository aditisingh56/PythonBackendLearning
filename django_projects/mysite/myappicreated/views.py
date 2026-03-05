from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):  # here, we have written request because every view receives a request, and his request is the input like parameters
    return HttpResponse("<h1>Hello, welcome to my website!</h1>")  # this will return a simple response when we go to the root page of the website. we can also return a template instead of a simple response by using render function and passing the request and the template name as arguments.