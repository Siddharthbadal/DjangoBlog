from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'body','email','name')




class PostSearchForm(forms.Form):
    q = forms.CharField()