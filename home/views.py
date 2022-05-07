from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    render(request, 'index.html')

def login(request):
    render(request, 'logout.html')

def logout(request):
    render(request, 'index.html')