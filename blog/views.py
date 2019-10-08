from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
from django.urls import reverse

# importing generic class view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        # obj = Article.objects.all(id=1)
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'article_create.html'
    queryset = Article.objects.all()

class ArticleDeleteView(DeleteView):
    form_class = ArticleForm
    template_name = 'article_delete.html'
    queryset = Article.objects.all()


    def get_object(self):
        # obj = Article.objects.all(id=1)
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

    def get_success_url(self):
        return reverse("blog:article_list")

class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = 'article_create.html'
    queryset = Article.objects.all()

    def get_object(self):
        # obj = Article.objects.all(id=1)
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
