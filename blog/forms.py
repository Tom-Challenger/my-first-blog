from django import forms 
from .models import Post #импортировать модель Post
#импортировать модуль Django.forms
class PostForm(forms.ModelForm):
	class Meta:  
		#какая модель будет использоваться для создания формы (model=Post)
		model = Post
		fields = ('title', 'text',)
