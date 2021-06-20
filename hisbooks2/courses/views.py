from django.http.response import HttpResponse
from django.shortcuts import render
import urllib.request
import json

# Create your views here.

def courseSearch(request):
    # return HttpResponse("<h1>this is course search<h1>")
    return render(request, 'coursepage.html', {})


 
