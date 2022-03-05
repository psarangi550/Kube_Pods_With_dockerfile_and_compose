from django.shortcuts import render
from django.http import HttpResponse


def index_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello There Good Morning</h1>")# Create your views here.
