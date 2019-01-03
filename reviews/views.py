from django.shortcuts import render
from first.forms import SelectionForm
from .models import Article
from django.http import HttpResponse
#Create your views here.

def index(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'reviews/index.html', {'articles':articles})

def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'reviews/article_detail.html', {'article':article})
