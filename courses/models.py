from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length = 120)
    lecturer = models.CharField(max_length = 20)
    students = models.IntegerField()

    def get_absolute_url(self):
        # return f"{self.id}/"
        return reverse("courses:course_detail", kwargs={"id":self.id})
