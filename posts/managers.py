from django.db import models


class PostManager(models.Manager):

    def some_next(self, created_at, main_category):
        '''Возвращаем несколько следующих срисовку'''
        some = 6
        return list(super().get_queryset().filter(
            enabled=True, created_at__lt=created_at,
            main_category=main_category).order_by('-created_at'))[:some]

    def some_previous(self, created_at, main_category):
        '''Возвращаем несколько предыдущих срисовку'''
        some = 6
        return list(super().get_queryset().filter(
            enabled=True, created_at__gt=created_at,
            main_category=main_category).order_by('-created_at'))[-some:]

    def next_(self, created_at, main_category):
        '''Возвращаем следующюю срисовку'''
        return super().get_queryset().filter(
            enabled=True, created_at__lt=created_at,
            main_category=main_category).order_by('-created_at').first()

    def previous(self, created_at, main_category):
        '''Возвращаем предыдущюю срисовку'''
        return super().get_queryset().filter(
            enabled=True, created_at__gt=created_at,
            main_category=main_category).order_by('-created_at').last()
