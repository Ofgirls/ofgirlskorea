from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    post_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Post
        fields = ('category', 'writer', 'post_password', 'title', 'text', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text', )


class PasswordCheckForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
