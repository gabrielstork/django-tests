from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'text',
        )

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'w-100 mb-2', 'placeholder': 'title',}
            ),
            'text': forms.Textarea(
                attrs={'class': 'w-100', 'placeholder': 'text'}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'text',
        )

        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'w-100', 'placeholder': 'comment', 'style': 'height: 100px;'}
            ),
        }
