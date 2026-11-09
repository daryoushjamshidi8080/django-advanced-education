from django import forms
from .models import Category, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['auther', 'title', 'content', 'status', 'category', 'published_date']