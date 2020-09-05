from django import forms
from .models import Comments
class CommentForm(forms.ModelForm):
    class Meta:
        models = Comments
        fields = ['Name', 'Title', 'Message']