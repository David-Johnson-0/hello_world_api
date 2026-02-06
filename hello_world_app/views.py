from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, World!</h1>" \
    "<p>Welcome to the Django Hello World Application" \
    "deployed from AWS EC2 instance to PostgreSQL database!" \
    "The Author of this application is David Johnson as part" \
    "of the class CSCI 4830.</p>")