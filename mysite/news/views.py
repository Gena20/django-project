from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import HashtagForm, ArticleForm, RubricForm
from .models import Article, Rubric, Hashtag


def index(request):
    context = make_default_context()
    return render(request, 'index.html', context)


def rubric(request, id):
    articles = Article.objects.filter(rubric=id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=id)

    context = make_default_context({'articles': articles, 'rubrics': rubrics, 'current_rubric': current_rubric})
    return render(request, 'rubric.html', context)


def article(request):
    context = make_default_context()
    return render(request, 'article.html', context)


def make_default_context(context={}):
    return {'rubrics': Rubric.objects.all()} | context


class HashtagCreateView(CreateView):
    form_class = HashtagForm
    template_name = 'create_form.html'
    success_url = '/news/index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a hashtag'
        return make_default_context(context)


class RubricCreateView(CreateView):
    form_class = RubricForm
    template_name = 'create_form.html'
    success_url = '/news/index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a rubric'
        return make_default_context(context)


class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'create_form.html'
    success_url = '/news/index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add an article'
        return make_default_context(context)