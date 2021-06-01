from django.core.management.base import BaseCommand, CommandError
from news.models import Article, Rubric, Hashtag
import os.path
import pandas as pd
from random import randrange


class Command(BaseCommand):
    help = 'Init articles'

    def add_arguments(self, parser):
        parser.add_argument('articles_data_filepath', type=str)

    def handle(self, *args, **options):
        articles_data_filepath = options['articles_data_filepath']
        project_dir = os.path.abspath(os.path.dirname(__name__))

        filepath = f'{project_dir}/{articles_data_filepath}'
        if not os.path.isfile(filepath):
            raise CommandError('Invalid filepath was given, file "%s" dose not exist' % filepath)

        articles = pd.read_csv(filepath, sep=';')
        for index, article in articles.iterrows():
            self.make_article(index, article)
            self.stdout.write(self.style.SUCCESS(f'{index}. Init article - {article["title"]}' ))

        self.stdout.write(self.style.SUCCESS('Successfully init %s articles' % len(articles)))

    def make_article(self, index, article_data):
        article = Article(
            pk=index,
            title=article_data['title'],
            keywords=article_data['keywords'],
            annotation=article_data['annotation']
        )

        try:
            rubric = Rubric.objects.get(pk=article_data['rubNum'])
        except Rubric.DoesNotExist:
            CommandError('Rubric "%s" does not exist' % article_data['rubNum'])
            return
        article.rubric = rubric

        try:
            hashtag_id = randrange(1, 13)
            hashtag = Hashtag.objects.get(pk=hashtag_id)
        except Hashtag.DoesNotExist:
            CommandError('Hashtag "%s" does not exist' % hashtag_id)
        article.hashtags.add(hashtag)

        article.save()