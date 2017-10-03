from django.shortcuts import render
from .models import Post
from django.utils import timezone # Подключение библиотеки работы со временем

# Create your views here.


def post_list(request): #reuest - это все что мы получили от пользателя через Инет
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
