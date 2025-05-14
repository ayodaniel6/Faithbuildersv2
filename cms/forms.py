from django import forms
from blog.models import Post
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30, 'class': 'tinymce-editor'}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'file', 'audio', 'tags', 'is_draft']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 p-4 rounded-md w-full text-2xl font-semibold',  # Larger text and padding
                'placeholder': 'Enter your post title here...'
            }),
            'tags': forms.TextInput(attrs={'placeholder': 'Add tags (comma separated)', 'class': 'border-gray-300 p-2 rounded-md w-full'}),
            'is_draft': forms.CheckboxInput(attrs={'class': 'form-checkbox text-blue-600'})
        }