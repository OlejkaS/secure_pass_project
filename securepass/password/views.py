from django.shortcuts import get_object_or_404, render

from .models import Password

menu = ['О сайте', 'Обратная связь', 'Войти', 'Калькулятор']

cat_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    context = {
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, 'passwords/index.html', context)


def about(request):
    context = {
        'about': 'Информация о сайте'
    }
    return render(request, 'passwords/about.html', context)


def password_generate(request):
    return render(request, 'passwords/generator.html')


def show_post(request, pass_slug):
    password = get_object_or_404(Password, slug=pass_slug)
    passw = Password.idx.all()
    data = {
        'title': password.title,
        'username': password.username,
        'time_create': password.time_create,
        'passw': passw
    }
    return render(request, 'passwords/pass.html', data)
