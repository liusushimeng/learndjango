from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def return_html(request):
    return HttpResponse('<h1>Hello Wang Wei</h1>')


