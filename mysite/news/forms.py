from django.forms import ModelForm
from .models import Article, Hashtag, Rubric


class HashtagForm(ModelForm):
    class Meta:
        model = Hashtag
        fields = '__all__'


class RubricForm(ModelForm):
    class Meta:
        model = Rubric
        fields = '__all__'


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

