from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse


class ArticleIndexView(View):
    def get(self, request):
        return render(
            request,
            'articles/index.html',
            {'text': 'Статьи'}
        )

def article_view(request, tags, article_id):
    text = f"Статья номер {article_id}. Тег {tags}"
    return render(  
        request,
        'articles/article.html',
        {'text': text}
    )

def home_redirect(request):
    return redirect(
        reverse('article', args=('python', 42))
    )