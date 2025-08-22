from django import forms
from .models import CounsellorRequest

INPUT_CLASSES = "w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 shadow-sm transition-all"

class CounsellorRequestForm(forms.ModelForm):
    class Meta:
        model = CounsellorRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Your Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'you@example.com'
            }),
            'message': forms.Textarea(attrs={
                'class': INPUT_CLASSES + " min-h-[120px]",
                'placeholder': 'Tell us what you need help with...'
            }),
        }
