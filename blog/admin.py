from django.contrib import admin
from .models import Article

# admin Interface for the article
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content'
    )

# Register your models here.
admin.site.register(Article, ArticleAdmin)