from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=255)

class Hashtag(models.Model):
    name = models.CharField(max_length=255)

class Article(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    annotation = models.TextField()
    hashtags = models.ManyToManyField(Hashtag)
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)
