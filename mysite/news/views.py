from django.shortcuts import render
from news.models import Article, Rubric, Hashtag


def index(request):
    context = make_default_context()
    return render(request, 'index.html', context)


def article(request):
    context = make_default_context()
    return render(request, 'article.html', context)


def make_default_context(context={}):
    return {'rubrics': Rubric.objects.all()} | context
