from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


from .models import Article

def index(request):
    
    article_list = Article.objects.all()
    template = loader.get_template('article/index.html')
    context = {
        'article_list': article_list,
    }
    return HttpResponse(template.render(context,request))
    

def details(request, article_id):
    article = Article.objects.get(pk=article_id)
    #article = Article.objects.all()[int(article_id)-1]
    template = loader.get_template('article/details.html')
    context = {
        'article': article
    }
    return HttpResponse(template.render(context,request))

    
