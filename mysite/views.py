from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'pages/landing.html')


def about(request):
    return render(request, 'pages/about.html')


def blog(request):
    return render(request, 'pages/blog.html')


def portfolio(request):
    return render(request, 'pages/portfolio.html')
