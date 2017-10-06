from django import forms 
from .models import Post, Comment
#импортировать модуль Django.forms
#импортировать модель Post
#импортировать модель Comment

class PostForm(forms.ModelForm):
	class Meta:  
		#какая модель будет использоваться для создания формы (model=Post)
		model = Post
		fields = ('title', 'text',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author', 'text',)
