from django import forms
from . import models

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = [
            'title',
            'body',
            'thumb'
        ]