from django.contrib import admin
from .models import Course

# admin interface for the model
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'lecturer',
        'students'
    )

# Register your models here.
admin.site.register(Course, CourseAdmin)
