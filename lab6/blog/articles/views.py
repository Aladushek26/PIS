from django.shortcuts import render
from .models import Article
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
User = get_user_model()




def article_list(request):
    posts = Article.objects.all().order_by('-created_date')  # Все статьи, сортировка по дате
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
    
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # проверка на уникальность названия
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                
                # если поля заполнены без ошибок и название уникально
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404
    
def auth(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            error = "Пароли не совпадают"
            return render(request, "auth.html", {"error": error})

        if User.objects.filter(username=username).exists():
            error = "Пользователь с таким именем уже существует"
            return render(request, "auth.html", {"error": error})

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("archive")  # Или на другую страницу
    else:
        # Эта ветка сработает при GET-запросе — просто показать форму
        return render(request, "auth.html")
