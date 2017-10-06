from django.contrib import admin

# Register your models here.

#from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)  # Регистрируем нашу модель - что бы она стала доступна на странице администрирования
admin.site.register(Comment)
