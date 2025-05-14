from django import forms
from .models import CounsellorRequest

class CounsellorRequestForm(forms.ModelForm):
    class Meta:
        model = CounsellorRequest
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Tell us what you need help with...'}),
        }
