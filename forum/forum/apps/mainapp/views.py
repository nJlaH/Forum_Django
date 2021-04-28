from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

def index(request):
    articles = Article.objects.order_by('Article_publication')[:5]
    return render(request, 'mainapp/list.html', {'articles': articles})  # видимо, путь идет от файла с шаблонами, который мы указали в settings ||| тут можно передать в шаблон переменную, которую мы можем указать строкой выше. Видимо, тут мы можем достать конкретную статью и обратиться к ее характеристикам!

def certain_article(request, a_id):
    try:
        a = Article.objects.get(id=a_id)
    except:
        raise Http404("Article is not found")

    comments_list = a.comment_set.order_by('-id')[:10]  # возвращает список комментариев к статье
    comments_number = len(comments_list)
    return render(request, 'mainapp/detail.html', {'article_from_certain_article': a, 'comments_list': comments_list, 'comments_number': comments_number})

def add_comment(request, a_id):
    try:
        a = Article.objects.get(id=a_id)
    except:
        raise Http404("Article is not found")

    a.comment_set.create(Comment_author=request.POST['comment_author'], Comment_text=request.POST['comment_text'])  # извлекаем данные из формы
    return HttpResponseRedirect(reverse('mainapp:certain_article', args=(a.id,)))  # редирект обратно, к ссылке аргументом прибавляем id статьи

def add_article(request):
    Article.objects.create(Article_title=request.POST['article_title'], Article_text=request.POST['article_text'])  # применяем метод .create(...) к объекту Article
    return HttpResponseRedirect(reverse('mainapp:index'))