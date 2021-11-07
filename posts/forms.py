
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Post Form"""
    class Meta:
        model = Post
        fields = ('text', 'group', 'image')
        labels = {'text': 'Текст записи', 'group': 'Сообщество'}
        widgets = {'text': forms.Textarea()}


class CommentForm(forms.ModelForm):
    """Comment Form"""
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Комментарий',}
        widgets = {'text': forms.Textarea({'rows': 3})}