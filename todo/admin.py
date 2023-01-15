from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date", )


admin.site.register(Post, PostAdmin)
