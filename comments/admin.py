from django.contrib import admin

from comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'user')
    list_display_links = ('post', )
    list_filter = ('created_at', 'user')
    readonly_fields = ['user', 'post', 'parent', 'created_at']

    search_fields = ['post__name']
