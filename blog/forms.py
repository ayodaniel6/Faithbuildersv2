from django import forms
from .models import Comment, Post
from ckeditor.widgets import CKEditorWidget


INPUT_CLASSES = "w-full px-4 py-2 mt-2 border rounded-xl bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-400 dark:bg-gray-900 dark:border-gray-700 dark:text-white"

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Write your comment here...',
                'rows': 4,
            }),
        }
        labels = {
            'content': '',
        }


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'file', 'audio', 'tags', 'is_draft', 'video_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'class': INPUT_CLASSES,
            'placeholder': 'Post Title',
        })

        self.fields['tags'].widget.attrs.update({
            'class': INPUT_CLASSES,
            'placeholder': 'Select tags...',
        })

        self.fields['video_url'].widget.attrs.update({
            'class': INPUT_CLASSES,
            'placeholder': 'Optional YouTube/Vimeo URL',
        })

        # For files (image, audio, file)
        file_classes = "mt-2 text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100"

        self.fields['image'].widget.attrs.update({'class': file_classes})
        self.fields['file'].widget.attrs.update({'class': file_classes})
        self.fields['audio'].widget.attrs.update({'class': file_classes})

        # Checkbox for drafts
        self.fields['is_draft'].widget.attrs.update({
            'class': "rounded text-indigo-600 focus:ring-indigo-500"
        })
