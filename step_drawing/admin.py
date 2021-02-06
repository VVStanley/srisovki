from mptt.admin import MPTTModelAdmin
from ckeditor.widgets import CKEditorWidget

from django.contrib import admin
from django.forms.fields import CharField

from step_drawing.models import \
    CategoryStepDrawingModel, PostStepDrawingModel,\
    ImagesPostDrawingModel, VideoPostModel


@admin.register(CategoryStepDrawingModel)
class CategoryStepDrawingAdmin(MPTTModelAdmin):

    mptt_level_indent = 20

    list_filter = ('enabled', 'show_main')
    list_display = ('name', 'position', 'enabled', 'show_main', 'created_at')
    list_display_links = ('name',)
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {"slug": ("name",)}

    search_fields = ['name']

    fieldsets = (
        ('Основное', {'fields': ('name', 'parent', 'position', 'enabled', 'image', 'image_menu')}),
        ('SEO', {'fields': ('title', 'h1', 'slug', 'description')}),
        ('Отображение на главной', {'fields': ('show_main', )}),
        ('Контент', {'fields': ('text1', 'text2')}),
        ('Дополнительно', {'fields': ('created_at', 'updated_at')}), )

    text1 = CharField(widget=CKEditorWidget())
    text2 = CharField(widget=CKEditorWidget())


class ImagesPostDrawingInline(admin.TabularInline):

    model = ImagesPostDrawingModel

    fieldsets = (
        ('Осносное', {'fields': ('position', 'steps')}),
        ('Контент', {'fields': ('text_up', 'image', 'text_down')})
    )

class VideoPostInline(admin.TabularInline):

    model = VideoPostModel

    fieldsets = (
        ('Ссылка на видео', {'fields': ('name', 'frame', )}),
    )


@admin.register(PostStepDrawingModel)
class PostStepDrawingAdmin(admin.ModelAdmin):

    list_display = ('name', 'enabled', 'main_category', 'created_at')
    list_display_links = ('name', )
    list_filter = ('created_at', 'enabled', 'main_category', )
    readonly_fields = ['like', 'click', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

    search_fields = ['name', ]

    fieldsets = (
        ('Основное', {'fields': ('enabled', 'position', 'image', 'level', 'execution_time', 'show_main')}),
        ('SEO', {'fields': ('title', 'name', 'slug', 'description')}),
        ('Зависимости', {'fields': ('main_category', 'categories')}),
        ('Контент', {'fields': ('text', )}),
        ('Дополнительно', {'fields': ('like', 'click', 'created_at', 'updated_at')})
    )

    text = CharField(widget=CKEditorWidget())

    inlines = [
        VideoPostInline,
        ImagesPostDrawingInline,
    ]