from django import forms
from blog.models import Post
from ckeditor.widgets import CKEditorWidget

# Reusable Tailwind style for consistency
INPUT_CLASSES = (
    "w-full px-4 py-2 rounded-xl border border-gray-300 focus:outline-none "
    "focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 shadow-sm "
    "transition duration-300 ease-in-out"
)

CHECKBOX_CLASSES = "form-checkbox h-5 w-5 text-indigo-500 rounded transition duration-300 ease-in-out"

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(attrs={
        'class': 'rounded-xl border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 shadow-sm transition-all duration-300'
    }))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'file', 'audio', 'tags', 'is_draft', 'video_url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES + " text-2xl font-semibold",
                'placeholder': 'Enter your post title here...'
            }),
            'tags': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Add tags (comma separated)'
            }),
            'is_draft': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASSES}),
            'video_url': forms.URLInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Paste video URL here (optional)'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': "mt-2 text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 "
                         "file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 transition"
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': "mt-2 text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 "
                         "file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 transition"
            }),
            'audio': forms.ClearableFileInput(attrs={
                'class': "mt-2 text-sm text-gray-600 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 "
                         "file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 transition"
            }),
        }
