from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, this is the index page!")
