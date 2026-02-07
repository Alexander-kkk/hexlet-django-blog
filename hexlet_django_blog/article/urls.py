from django.urls import path
from .views import ArticleIndexView
from . import views

urlpatterns = [
    path('', ArticleIndexView.as_view(), name='article_index'),
    path('<str:tags>/<int:article_id>/', views.article_view, name='article'),
]