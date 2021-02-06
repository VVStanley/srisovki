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

User = get_user_model()


def image_path_category(instance, filename):
    return f'step_drawing_category/{str(instance.slug)}{get_extension(filename)}'

def image_menu_path_category(instance, filename):
    return f'step_drawing_category/{str(instance.slug)}_menu{get_extension(filename)}'


class CategoryStepDrawingModel(MPTTModel):

    class Meta:
        verbose_name = 'Категория пошаговое рисование'
        verbose_name_plural = 'Категории пошаговых рисований'
        db_table = 'step_category'

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

    image = models.FileField(upload_to=image_path_category, null=True, blank=True, verbose_name='Осносное изображение')
    image_menu = models.FileField(upload_to=image_menu_path_category, null=True, blank=True,
        verbose_name='Картинка в меню', help_text='Иконка в меню')
    show_main = models.BooleanField(default=False, verbose_name='Отображать на главной или нет')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def image_path(self):
        return f'{settings.MEDIA_URL}{self.image}'

    def image_menu_path(self):
        return f'{settings.MEDIA_URL}{self.image_menu}'

    def get_alt(self):
        return f'альт картинки'

    def get_title(self):
        return f'Ститле картинке'

    def get_absolute_url(self):
        return reverse('step_drawing:category_or_post', args=[str(self.slug)])


def image_path_post(instance, filename):
    '''Фомируем путь загрузки картинки поста'''
    return f'step_drawing_posts/{str(instance.slug)}{get_extension(filename)}'


class PostStepDrawingModel(models.Model):

    class Meta:
        verbose_name = 'Запись пошаговое рисование'
        verbose_name_plural = 'Записи пошаговое рисование'
        db_table = 'step_posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    wishlist = models.ManyToManyField(User)

    position = models.IntegerField(default=0, verbose_name='Позиция')
    enabled = models.BooleanField(
        default=False,
        choices=settings.STATUS_CHOICES,
        verbose_name='Опубликовано',
        help_text='Отображать/неотображать пост'
    )
    categories = TreeManyToManyField(
        CategoryStepDrawingModel,
        verbose_name='Категории',
        related_name='posts_cat',
        blank=True
    )
    main_category = TreeForeignKey(
        CategoryStepDrawingModel,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Основная категория',
        related_name='posts_main',
        help_text='Используется для хлебных крошек'
    )

    name = models.CharField(max_length=250, unique=True, verbose_name='h1', help_text='Название поста')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url(slug)')
    title = models.CharField(max_length=250, default='Картинка для срисовки')
    description = models.TextField(null=True, blank=True)

    text = RichTextField(null=True, blank=True, verbose_name='Текст')

    show_main = models.BooleanField(default=False, verbose_name='Отображать на главной или нет')
    execution_time = models.CharField(max_length=50, verbose_name='Время на выполнения', null=True, blank=True)
    level = models.CharField(max_length=100, verbose_name='Уровень сложности', choices=settings.LEVEL_CHOICES)

    image = models.ImageField(
        upload_to=image_path_post,
        verbose_name='Основное изображение',
        help_text='Отображаестя в категории'
    )
    image_thumb_300 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 225)],
        format='JPEG', options={'quality': 65}
    )
    image_thumb_200 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 150)],
        format='JPEG', options={'quality': 60}
    )

    like = models.IntegerField(default=0, verbose_name='Лайки', help_text='Общее количество лайков')
    click = models.IntegerField(default=0, verbose_name='Клики', help_text='Общее количество кликов')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def save(self, *args, **kwargs):
        if not self.id:
            self.like = get_random_number(0, 3)
            self.click = get_random_number(0, 6)
        super(PostStepDrawingModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('step_drawing:category_or_post', args=[str(self.slug)])

    def image_path(self):
        return f'{settings.MEDIA_URL}{self.image}'


def images_path_post(instance, filename):
    '''Фомируем путь загрузки картинки поста'''
    return f'step_drawing_posts/{str(instance.post.slug)}{get_extension(filename)}'


class VideoPostModel(models.Model):

    class Meta:
        verbose_name = 'Видео для поста обучения'
        verbose_name_plural = 'Видео для поста обучения'
        db_table = 'step_videos'

    def __str__(self):
        return f'Видео для {self.post}'

    post = models.ForeignKey('PostStepDrawingModel', related_name='videos', on_delete=models.CASCADE)

    frame = models.CharField(max_length=350, verbose_name='Видео')
    name = models.CharField(max_length=250, verbose_name='Название')


class ImagesPostDrawingModel(models.Model):

    class Meta:
        verbose_name = 'Изображение для постов пошагового рисования'
        verbose_name_plural = 'Изображения для постов пошагового рисования'
        db_table = 'step_images'
        ordering = ['position']

    def __str__(self):
        return f'{self.steps} для {self.post}'

    position = models.IntegerField(default=0, verbose_name='Сортировка')
    steps = models.CharField(max_length=30, verbose_name='Шаг/Этап')

    post = models.ForeignKey('PostStepDrawingModel', related_name='images', on_delete=models.CASCADE)

    text_up = RichTextField(null=True, blank=True, verbose_name='Текст сверху')
    text_down = RichTextField(null=True, blank=True, verbose_name='Текст внизу')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    image = models.FileField(
        upload_to=images_path_post,
        null=True, blank=True,
        verbose_name='Изображение',
    )
    image_thumb_300 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 225)],
        format='JPEG', options={'quality': 65}
    )
    image_thumb_200 = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 150)],
        format='JPEG', options={'quality': 60}
    )

    def image_path(self):
        return f'{settings.MEDIA_URL}{self.image}'



@receiver(pre_delete, sender=ImagesPostDrawingModel)
def image_posts_delete(sender, instance, **kwargs):
    '''Удаляем картинки с постов, при удалении поста'''
    if instance.image:
        instance.image.delete()


@receiver(pre_delete, sender=PostStepDrawingModel)
def posts_im_delete(sender, instance, **kwargs):
    '''Удаляем картинки с постов, при удалении поста'''
    if instance.image:
        instance.image.delete()


@receiver(pre_delete, sender=CategoryStepDrawingModel)
def cat_image_delete(sender, instance, **kwargs):
    '''Удаляем картинки с категории, при удалении категории'''
    if instance.image:
        instance.image.delete()
    if instance.image_menu:
        instance.image_menu.delete()