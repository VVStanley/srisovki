from django.contrib import admin

from front.models import FeedbackModel


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = ('email', 'name')
    list_display_links = ('email', )

    list_filter = ('created_at', )
