from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),  # Корень приложения — список статей
]
