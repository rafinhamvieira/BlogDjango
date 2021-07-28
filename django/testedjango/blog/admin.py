from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    listDisplay = ("title","slug","author", "created","updated")
    prepopulated_fields = {"slug":("title",)}