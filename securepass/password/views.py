from django.shortcuts import render


def index(request):
    return render(request, 'passwords/index.html')


def about(request):
    pass
