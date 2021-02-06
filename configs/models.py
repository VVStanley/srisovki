from solo.models import SingletonModel
from ckeditor.fields import RichTextField

from django.db import models


class StepDrawingConfiguration(SingletonModel):
    
    class Meta:
        verbose_name = 'Обучение настройка'
        db_table = 'step_config'

    def __str__(self):
        return 'Обучение настройка'

    caption = models.CharField(max_length=150, verbose_name='Заголовок')
    text1 = RichTextField(null=True, blank=True, verbose_name='Текст 1')


class Metrics(SingletonModel):

    class Meta:
        verbose_name = "Метрики, аналитики"

    def __str__(self):
        return "Метрики, аналитики"

    yandex = models.TextField(verbose_name='Метрика яндекса', null=True, blank=True)
    google_analytics = models.TextField(verbose_name='Гугл аналитика', null=True, blank=True)
    google_adSense = models.TextField(verbose_name='Гугл адсенс', null=True, blank=True)


class ReklamaAll(SingletonModel):

    class Meta:
        verbose_name = "Реклама все страницы"

    def __str__(self):
        return "Реклама все страницы"

    top_reklama_block = models.TextField(verbose_name='Код рекламы верхний блок', null=True, blank=True)
    sidebar_reklama_block = models.TextField(verbose_name='Код рекламы сайтбар', null=True, blank=True)


class ReklamaCategory(SingletonModel):

    class Meta:
        verbose_name = "Реклама категории"

    def __str__(self):
        return "Реклама категории"

    first_reklama_block = models.TextField(verbose_name='Код рекламы первый блок', null=True, blank=True)
    second_reklama_block = models.TextField(verbose_name='Код рекламы второй блок', null=True, blank=True)
    third_reklama_block = models.TextField(verbose_name='Код рекламы третий блок', null=True, blank=True)
    fourth_reklama_block = models.TextField(verbose_name='Код рекламы четвертый блок', null=True, blank=True)
    fifth_reklama_block = models.TextField(verbose_name='Код рекламы пятый блок', null=True, blank=True)


class ReklamaStepPosts(SingletonModel):

    class Meta:
        verbose_name = "Реклама пошаговые посты обучения"
        db_table = 'step_reklama'

    def __str__(self):
        return "Реклама пошаговые посты обучения"

    block1 = models.TextField(verbose_name='Первый блок', null=True, blank=True)
    block2 = models.TextField(verbose_name='Второй блок', null=True, blank=True)
    block3 = models.TextField(verbose_name='Третий блок', null=True, blank=True)
    block4 = models.TextField(verbose_name='Четвертый блок', null=True, blank=True)
    block5 = models.TextField(verbose_name='Пятый блок', null=True, blank=True)
    block6 = models.TextField(verbose_name='Шестой блок', null=True, blank=True)
    block7 = models.TextField(verbose_name='Седьмой блок', null=True, blank=True)
    block8 = models.TextField(verbose_name='Восьмой блок', null=True, blank=True)


class ReklamaPosts(SingletonModel):

    class Meta:
        verbose_name = "Реклама посты"

    def __str__(self):
        return "Реклама посты"

    left_reklama_block = models.TextField(verbose_name='Код рекламы левый блок', null=True, blank=True)
    right_reklama_block = models.TextField(verbose_name='Код рекламы правый блок', null=True, blank=True)
    down_reklama_block = models.TextField(verbose_name='Код рекламы нижний блок', null=True, blank=True)


class PostConfiguration(SingletonModel):

    class Meta:
        verbose_name = "Настройки поста"

    def __str__(self):
        return "Настройки поста"

    new_post_days = models.PositiveSmallIntegerField(
        verbose_name="Дней", default=30,
        help_text='Кол-во дней пост считается новым (badge)'
    )
    post_popular = models.PositiveSmallIntegerField(
        verbose_name="Кол-во просмотров", default=500,
        help_text='Пост считается просматриваемый (badge)'
    )
    post_best = models.PositiveSmallIntegerField(
        verbose_name="Кол-во лайков", default=10,
        help_text='Пост считается отлайканым (badge)'
    )

class HomeConfiguration(SingletonModel):

    class Meta:
        verbose_name = "Главная страница"

    def __str__(self):
        return "Главная страница"

    caption = models.CharField(max_length=150, verbose_name='Заголовок')

    text1 = RichTextField(null=True, blank=True, verbose_name='Текст 1')
    text2 = RichTextField(null=True, blank=True, verbose_name='Текст 2')

    