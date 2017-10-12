from django.contrib import admin
from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['published_date']}),
        ('Post 내용', {'fields': ['writer', 'title', 'text']}),
    ]
    list_display = ('title', 'published_date')
    list_filter = ['published_date']
    # 좋아요 개수, 코멘트 개수로도 필터할거임


class CommentAdmin(admin.ModelAdmin):
    fields = ['created_date', 'author', 'text', ]
    # post의 pk값도 보여줘야겠음
    # 얘도 좋아요 수로 필터링할 예정

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
