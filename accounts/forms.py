from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import Profile

class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg',
            'placeholder': 'Enter password'
        })
    )
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg',
            'placeholder': 'First name (optional)'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg',
            'placeholder': 'Enter username'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg',
            'placeholder': 'Enter email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg',
            'placeholder': 'Username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border rounded-lg',
            'placeholder': 'Password'
        }))


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, label='First Name')
    username = forms.CharField(label='Username', disabled=True)
    email = forms.EmailField(label='Email', disabled=True)

    class Meta:
        model = User
        fields = ['first_name', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500',
                'placeholder': 'First Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md bg-gray-100 cursor-not-allowed text-gray-500',
                'placeholder': 'Username',
                'readonly': True  # Extra protection to ensure it’s uneditable
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md bg-gray-100 cursor-not-allowed text-gray-500',
                'readonly': True  # Extra protection to ensure it’s uneditable
            }),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500',
                'placeholder': 'Write a short bio...'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-purple-50 file:text-purple-700 hover:file:bg-purple-100',
                'accept': 'images/*',
                'onchange': 'previewAvatar(event)'
            }),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:outline-none',
            'placeholder': 'Enter current password'
        })
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:outline-none',
            'placeholder': 'Enter new password'
        })
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:outline-none',
            'placeholder': 'Confirm new password'
        })
    )