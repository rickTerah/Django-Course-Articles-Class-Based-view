from django import forms
from .models import Course

# Create your forms here.
class CourseForm(forms.ModelForm):
    title = forms.CharField()
    lecturer = forms.CharField()
    students = forms.IntegerField()

    class Meta:
        model = Course
        fields = [
            'title',
            'lecturer',
            'students'
        ]
