from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
     list_display = ['title','create_date']

     class Meta:
          model = Post

admin.site.register(Post)