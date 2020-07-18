from django import forms
from .models import Comment, Post

class CommentEditForm(forms.Form):
        text = forms.CharField(max_length=50,required=True)
        

class CommentForm(forms.ModelForm):
	body = forms.CharField(max_length=5000,required=True)

	class Meta:
		model = Comment
		fields = ('body',)