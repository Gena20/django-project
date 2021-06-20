from django.urls import path
from . import views
from .views import HashtagCreateView, RubricCreateView, ArticleCreateView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('rubrics/<int:id>/', views.rubric, name='rubric'),
    path('article/', views.article, name='article'),
    path('add-hashtag/', HashtagCreateView.as_view(), name='add-hashtag'),
    path('add-rubric/', RubricCreateView.as_view(), name='add-rubric'),
    path('add-article/', ArticleCreateView.as_view(), name='add-article'),
]
