from django import forms
from .models import Comment, Post
from tinymce.widgets import TinyMCE  # Import TinyMCE widge

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:bg-gray-800 dark:text-white',
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }
        labels = {
            'content': '',
        }


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))  # Apply TinyMCE to the content field
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'file', 'audio', 'tags', 'is_draft']