from django.contrib import admin
from .models import Category, Post, Comment


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ['id', 'name', 'slug']
    list_editable = ['name', 'slug']
    search_fields = ['name']
    ordering = ['name']


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['published_date']}),
        ('Post 내용', {'fields': ['writer', 'title', 'text', 'post_password']}),
    ]
    list_display = ('title', 'published_date', 'category', 'post_password')
    list_display_links = ['title']
    list_filter = ['published_date', 'category']
    list_editable = ['category',]
    search_fields = ['title', 'text', ]
    ordering = ['-published_date']
    # 좋아요 개수, --> 안되고,
    # 코멘트 개수로도 필터할거임


class CommentAdmin(admin.ModelAdmin):
    fields = ['created_date', 'author', 'text', ]
    # post의 pk값도 보여줘야겠음
    # 얘도 좋아요 수로 필터링할 예정

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
