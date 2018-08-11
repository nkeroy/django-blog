from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


from .models import Article
from .models import Comment

def index(request):
    
    article_list = Article.objects.all()
    template = loader.get_template('article/index.html')
    context = {
        'article_list': article_list,
    }
    return HttpResponse(template.render(context,request))
    

def details(request, article_id):
    article = Article.objects.get(pk=article_id)
    comment_list = Comment.objects.filter(article=article) # get comments for the specific article
    template = loader.get_template('article/details.html')
    context = {
        'article': article,
	'comment_list': comment_list
    }
    return HttpResponse(template.render(context,request))

    
