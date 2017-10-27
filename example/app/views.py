from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def app(request):
    return render(request, 'app.html')
