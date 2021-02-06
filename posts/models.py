import os
from PIL import Image
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_delete

from utils.file import get_extension
from utils.rand import get_random_number
from utils.text import translite_slug
from posts.managers import PostManager
from configs.models import PostConfiguration

User = get_user_model()


def image_path_category(instance, filename):
    return f'category/{str(instance.slug)}{get_extension(filename)}'

def image_main_path_category(instance, filename):
    return f'category/{str(instance.slug)}_main{get_extension(filename)}'

def image_menu_path_category(instance, filename):
    return f'category/{str(instance.slug)}_menu{get_extension(filename)}'


class Category(MPTTModel):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['position']

    def __str__(self):
        return self.name

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    name = models.CharField(max_length=100, unique=True, verbose_name='Наименование')
    position = models.IntegerField(default=0, verbose_name='Позиция')
    enabled = models.BooleanField(default=False, choices=settings.STATUS_CHOICES,
        verbose_name='Включено', help_text='Отображать/неотображать категорию')
    text1 = RichTextField(null=True, blank=True, verbose_name='Текст 1')
    text2 = RichTextField(null=True, blank=True, verbose_name='Текст 2')

    h1 = models.CharField(max_length=250)
    title = models.CharField(max_length=250, default='Картинки для срисовки')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url(slug)', help_text='Ссылка на категорию')
    description = models.TextField(null=True, blank=True)

    image = models.FileField(upload_to=image_path_category, null=True, blank=True,
        verbose_name='Основное изображение', help_text='Отображается в категории')
    image_menu = models.FileField(upload_to=image_menu_path_category, null=True, blank=True,
        verbose_name='Картинка в меню', help_text='Иконка в меню')
    show_main = models.BooleanField(default=False, verbose_name='Отображать на главной или нет')
    image_main = models.FileField(upload_to=image_main_path_category, null=True, blank=True,
        verbose_name='Картинка на главной', help_text='Отображается на главной')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def image_path(self):
        return f'{settings.MEDIA_URL}{self.image}'

    def image_menu_path(self):
        return f'{settings.MEDIA_URL}{self.image_menu}'

    def image_main_path(self):
        return f'{settings.MEDIA_URL}{self.image_main}'

    def get_alt(self):
        return f'Срисовки {self.name.lower()} - распечатать, скачать бесплатно'

    def get_title(self):
        return f'Срисовки {self.name.lower()}'

    def get_absolute_url(self):
        return reverse('posts:category', args=[str(self.slug)])


def image_path_post(instance, filename):
    '''Фомируем путь загрузки картинки'''
    return f'{get_path_img(instance)}{get_extension(filename)}'


def get_path_img(instance):
    '''
        Посты юзеров - posts_users/ имя юзера / пост слаг
        Посты админа - posts_admins/ майн категория / пост слаг
    '''
    if instance.user.is_staff or instance.user.is_superuser:
        return f'posts_admins/{translite_slug(str(instance.main_category.slug))}/{str(instance.slug)}'
    return f'posts_users/{translite_slug(str(instance.user))}/{str(instance.slug)}'


class Post(models.Model):

    objects = models.Manager()
    get = PostManager()

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_at']

    def __str__(self):
        '''Возвращаем h1'''
        if self.user.is_superuser or self.user.is_staff:
            return self.name
        return f'{self.name} - от {self.user}'

    wishlist = models.ManyToManyField(User)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    position = models.IntegerField(default=0, verbose_name='Позиция')
    enabled = models.BooleanField(
        default=False, choices=settings.STATUS_CHOICES,
        verbose_name='Опубликовано', help_text='Отображать/неотображать пост')
    categories = TreeManyToManyField(
        Category, verbose_name='Категории', related_name='posts_cat', blank=True)
    main_category = TreeForeignKey(
        Category, on_delete=models.CASCADE, null=True,
        verbose_name='Основная категория', related_name='posts_main',
        help_text='Используется для хлебных крошек')

    name = models.CharField(max_length=250, unique=True, verbose_name='h1', help_text='Название поста')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url(slug)')
    title = models.CharField(max_length=250, default='Картинка для срисовки')
    description = models.TextField(null=True, blank=True)

    text = models.TextField(null=True, blank=True, verbose_name='Текст')

    image = models.ImageField(
        upload_to=image_path_post, verbose_name='Изображение',
        help_text='Ожидается изображение 800х800 jpeg')
    image_thumb_300 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG', options={'quality': 65})
    image_thumb_200 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='JPEG', options={'quality': 60})
    image_thumb_100 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 100)],
        format='JPEG', options={'quality': 60})

    like = models.IntegerField(default=0, verbose_name='Лайки', help_text='Общее количество лайков')
    click = models.IntegerField(default=0, verbose_name='Клики', help_text='Общее количество кликов')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def save(self, *args, **kwargs):
        if not self.id and (self.user.is_staff or self.user.is_superuser):
            self.like = get_random_number(0, 3)
            self.click = get_random_number(0, 6)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:post', args=[str(self.slug)])

    def image_path(self):
        return f'{settings.MEDIA_URL}{self.image}'

    def download_name(self):
        return f'{self.name.replace(" ", "_")}-картинки_для_срисовки_рф'

    def get_alt(self):
        if self.user.is_superuser or self.user.is_staff:
            return f'{self.name.lower()} - распечатать, скачать бесплатно'
        return f'{self.name} срисовал {self.user}'

    def get_title(self):
        if self.user.is_superuser or self.user.is_staff:
            return f'Срисовка {self.name.lower()}'
        return f'Срисовка {self.name.lower()} от {self.user}'


@receiver(pre_delete, sender=Category)
def cat_image_delete(sender, instance, **kwargs):
    '''Удаляем картинки с категории, при удалении категории'''
    if instance.image:
        instance.image.delete()
    if instance.image_main:
        instance.image_main.delete()
    if instance.image_menu:
        instance.image_menu.delete()


@receiver(pre_delete, sender=Post)
def post_image_delete(sender, instance, **kwargs):
    '''Удаляем картинки с поста, при удалении поста'''
    if instance.image:
        thumb_path = f'{settings.MEDIA_ROOT}/{get_path_img(instance)}'
        thumb_extension = get_extension(str(instance.image))
        try:
            os.remove(f'{thumb_path}_300{thumb_extension}')
        except FileNotFoundError:
            pass
        try:
            os.remove(f'{thumb_path}_200{thumb_extension}')
        except FileNotFoundError:
            pass
        try:
            os.remove(f'{thumb_path}_100{thumb_extension}')
        except FileNotFoundError:
            pass
        instance.image.delete()
