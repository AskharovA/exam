from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body', )
    list_display = ['title', 'author', 'category', 'created']
    list_display_links = ['title']
    list_filter = ['created', 'category']
    list_editable = ['category']
    raw_id_fields = ['author']
    date_hierarchy = 'created'
    ordering = ['-created']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'body']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created']
    list_filter = ['created']
    ordering = ['created']
