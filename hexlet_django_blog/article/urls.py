from django.urls import path
from hexlet_django_blog.article.views import ArticleFormCreateView, ArticleIndexView, ArticleView


urlpatterns = [
    path('', ArticleIndexView.as_view(), name='article_index'),
    path('<int:id>/', ArticleView.as_view(), name='article'),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
]