from django.shortcuts import render
from .models import Article

# Create your views here.
def articles(request):
    q = request.GET.get('q') # request.GET is a dictionary-like object that contains all the GET parameters from the URL. We use the get method to retrieve the value of the 'q' parameter. If 'q' is not present in the URL, it will return None.
    if q is not None:
        try:
            articles = Article.objects.filter(id=q)
        except Article.DoesNotExist:
            articles = None
    else:
        articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})



def New(request):
    article = Article.objects.create(title='', content='')
    return render(request, 'articles/create.html', {'article': article})

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        return render(request, 'articles/details.html', {'article': article})
    else:
        return render(request, 'articles/create.html', {'article': None})

def article(request, id=None):
    if id is None:
        return render(request, 'articles/details.html', {'article': None})
    
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        article = None
    
    return render(request, 'articles/details.html', {'article': article})