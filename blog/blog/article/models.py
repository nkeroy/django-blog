from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    main_body = models.CharField(max_length=1000)
    published_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.title 
