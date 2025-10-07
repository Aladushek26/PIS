from django.shortcuts import render
from .models import Article

def article_list(request):
    posts = Article.objects.all().order_by('-created_date')  # Все статьи, сортировка по дате
    return render(request, 'archive.html', {'posts': posts})
# Create your views here.
