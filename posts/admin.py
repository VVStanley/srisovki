from mptt.admin import MPTTModelAdmin
from ckeditor.widgets import CKEditorWidget

from django.urls import path
from django.contrib import admin
from django.contrib import messages
from django.shortcuts import redirect
from django.forms.fields import CharField

from posts.models import Post, Category
from utils.file import get_name_file
from utils.text import translite_slug


def make_published(modeladmin, request, queryset):
    queryset.update(enabled=True)

make_published.short_description = "Опублковать выбраные"


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):

    mptt_level_indent = 20
    change_form_template = 'admin/category_change.html'

    list_filter = ('created_at', 'show_main', 'enabled', )
    list_display = ('name', 'position', 'enabled', 'show_main', 'created_at')
    list_display_links = ('name',)
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {"slug": ("name",)}

    search_fields = ['name']

    fieldsets = (
        ('Основное', {'fields': ('name', 'parent', 'position', 'enabled', 'image_menu')}),
        ('SEO', {'fields': ('title', 'h1', 'slug', 'description')}),
        ('Отображение на главной', {'fields': ('show_main', 'image_main')}),
        ('Контент', {'fields': ('image', 'text1', 'text2')}),
        ('Дополнительно', {'fields': ('created_at', 'updated_at')}), )

    text1 = CharField(widget=CKEditorWidget())
    text2 = CharField(widget=CKEditorWidget())

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:id_cat>/change/load_posts_images/', self.load_posts_images)]
        return custom_urls + urls
    
    def get_title(self, name):
        return f'Картинка {name.lower()} &#10084; для срисовки'

    def get_description(self, name, main_category):
        return f'Срисуй красивый рисунок {name.lower()} &#11088; карандашом в тетрадь &#127942;. Отличная картинка {name.lower()} для детей, девочек &#128587; и мальчиков &#129312;. Скачай и распечатай легкие рисунки на сайте картинки-для-срисовки.рф'

    def load_posts_images(self, request, id_cat):
        images = request.FILES.getlist('post_images')
        error = False
        error_message = 'Не загружено: '
        for image in images:
            name = get_name_file(image)
            main_category = Category.objects.get(id=id_cat)
            try:
                post = Post.objects.create(
                    user=request.user,
                    main_category=main_category,
                    name=name,
                    image=image,
                    slug=translite_slug(name),
                    title=self.get_title(name),
                    description=self.get_description(name, main_category),
                    enabled=True
                )
                post.categories.set(main_category.get_ancestors(include_self=True))
                post.save()
            except Exception as e:
                error = True
                error_message += f'{image}; '
        if error_message:
            self.message_user(request, error_message, level=messages.ERROR)
        else:
            self.message_user(request, 'Все загружено!')
        return redirect('/manatee/posts/category/')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('name', 'user', 'enabled', 'main_category', 'created_at')
    list_display_links = ('name', )
    list_filter = ('created_at', 'enabled', 'main_category', )
    readonly_fields = ['like', 'click', 'created_at', 'updated_at']
    prepopulated_fields = {"slug": ("name",)}
    actions = [make_published]

    search_fields = ['name', ]

    fieldsets = (
        ('Основное', {'fields': ('enabled', 'position')}),
        ('SEO', {'fields': ('title', 'name', 'slug', 'description')}),
        ('Зависимости', {'fields': ('main_category', 'categories')}),
        ('Контент', {'fields': ('image', 'text')}),
        ('Дополнительно', {'fields': ('user', 'like', 'click', 'created_at', 'updated_at')}), )
