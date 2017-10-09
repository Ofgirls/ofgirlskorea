from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('writer', 'title', 'text', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', )
