from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'pages/landing.html')


def about(request):
    return render(request, 'pages/about.html')


def blog(request):
    blog_pages = [{
        'filename': '1.html',
        'title': 'Test',
        'post_date': '12/13/18',
        },
        {
        'filename': '2.html',
        'title': 'Test2',
        'post_date': '12/14/18',
        },
    ]
    context = {
        'blog_pages': blog_pages,
    }
    return render(request, 'pages/blog.html', context)


def blog_post(request, filename):
    blog_pages = [{
        'filename': '1.html',
        'title': 'Test',
        'post_date': '12/13/18',
        },
        {
        'filename': '2.html',
        'title': 'Test2',
        'post_date': '12/14/18',
        },
    ]
    context = {
        'blog_pages': blog_pages,
        'filename': filename,
    }
    return render(request, 'pages/blog_post.html', context)


def portfolio(request):
    return render(request, 'pages/portfolio.html')
