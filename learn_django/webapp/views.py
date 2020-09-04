from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<H2> Hey Welcome to my app</H2>')


