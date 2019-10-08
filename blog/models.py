from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 20)
    content = models.TextField()
    active = models.BooleanField()

    def get_absolute_url(self):
        # return f"{self.id}/"
        return reverse("blog:article_detail", kwargs = {"id": self.id})