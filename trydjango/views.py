
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string, get_template
from django.shortcuts import render

# def home_view(request):
#   first_article = Article.objects.get(id=1)
#   all_articles = Article.objects.all()

#   # This is a more manual way of rendering a template, but it is not recommended.
#   # html_string = render_to_string('home-view.html', {'first_article': first_article})
#   # return HttpResponse(html_string)

#   # This is a more manual way of rendering a template, but it is not recommended.
#   # template = get_template('home-view.html')
#   # html_string = template.render({'first_article': first_article})
#   # return HttpResponse(html_string)

#   # This is the recommended way of rendering a template. It is more concise and easier to read.
#   return render(request, 'home-view.html', {'first_article': first_article, 'all_articles': all_articles})