from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница сообщества group
    # Конвертор slug ожидает строку из букв и цифр
    path('group/<slug:slug>/', views.group_posts),
    ]
