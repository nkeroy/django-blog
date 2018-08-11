from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    main_body = models.CharField(max_length=1000)
    published_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.title 


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.text


