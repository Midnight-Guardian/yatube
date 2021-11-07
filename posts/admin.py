from django.contrib import admin
from .models import Post, Comment, Group
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """Post Admin Model"""
    list_display = ("id", "text", "pub_date", "author")
    search_fields = ("text",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):
    """Comment Admin Model"""
    list_display = ("id", "text", "author",)
    search_fields = ("author",)
    list_filter = ("post",)
    empty_value_display = "-пусто-"


class GroupAdmin(admin.ModelAdmin):
    """Group Admin Model"""
    list_display = ("id", "title")


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Group, GroupAdmin)
