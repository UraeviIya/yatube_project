from django.shortcuts import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница с записью
def group_posts_page(request, slug):
    return HttpResponse(f'Какая-то запись {slug}')
