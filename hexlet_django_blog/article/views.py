from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse



from hexlet_django_blog.article.forms import ArticleForm
from hexlet_django_blog.article.models import Article



class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:5]
        form = ArticleForm()
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles,
                'form': form,
            },
        )
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('article_index'))
        articles = Article.objects.all()[:5]
        return render(
            request,
            'articles/index.html',
            context={
                'articles': articles,
                'form': form,
            },
        )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'articles/show.html',
            context={'article': article}
        )

# def home_redirect(request):
#     return redirect(
#         reverse('article', args=('python', 42))
#     )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            return redirect('article_index') # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})