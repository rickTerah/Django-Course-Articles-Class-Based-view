from django import forms
from .models import Article

# Create your forms here.
class ArticleForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget = forms.Textarea())
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]