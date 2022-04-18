from django import forms
from .models import Account
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, UsernameField
)


class LogInForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={'class': 'w-100 mb-2', 'placeholder': 'username'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'w-100 mb-2', 'placeholder': 'password'}
        ),
    )


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'w-100 mb-2', 'placeholder': 'new password'}
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'w-100 mb-2', 'placeholder': 'confirm password'}
        )
    )

    class Meta(UserCreationForm.Meta):
        model = Account
        fields = (
            'username',
            'email',
        )

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'w-100 mb-2', 'placeholder': 'new username'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'w-100 mb-2', 'placeholder': 'email'}
            ),
        }
