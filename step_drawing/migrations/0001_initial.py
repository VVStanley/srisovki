# Generated by Django 3.0.2 on 2020-04-16 15:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import step_drawing.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryStepDrawingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Наименование')),
                ('position', models.IntegerField(default=0, verbose_name='Позиция')),
                ('enabled', models.BooleanField(choices=[(True, 'Опубликовано'), (False, 'Не опубликовано')], default=False, help_text='Отображать/неотображать категорию', verbose_name='Включено')),
                ('text1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст 1')),
                ('text2', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст 2')),
                ('h1', models.CharField(max_length=250)),
                ('title', models.CharField(default='Картинки для срисовки', max_length=250)),
                ('slug', models.SlugField(help_text='Ссылка на категорию', max_length=100, unique=True, verbose_name='Url(slug)')),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, help_text='Отображается в категории', null=True, upload_to=step_drawing.models.image_path_category, verbose_name='Основное изображение')),
                ('image_menu', models.FileField(blank=True, help_text='Иконка в меню', null=True, upload_to=step_drawing.models.image_menu_path_category, verbose_name='Картинка в меню')),
                ('show_main', models.BooleanField(default=False, verbose_name='Отображать на главной или нет')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='step_drawing.CategoryStepDrawingModel')),
            ],
            options={
                'verbose_name': 'Категория пошаговое рисование',
                'verbose_name_plural': 'Категории пошаговых рисований',
            },
        ),
        migrations.CreateModel(
            name='PostStepDrawingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0, verbose_name='Позиция')),
                ('enabled', models.BooleanField(choices=[(True, 'Опубликовано'), (False, 'Не опубликовано')], default=False, help_text='Отображать/неотображать пост', verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='Название поста', max_length=250, unique=True, verbose_name='h1')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url(slug)')),
                ('title', models.CharField(default='Картинка для срисовки', max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('level', models.CharField(choices=[(1, 'Легко'), (2, 'Средне'), (3, 'Сложно')], max_length=100, verbose_name='Уровень сложности')),
                ('image', models.ImageField(help_text='Отображаестя в категории', upload_to=step_drawing.models.image_path_post, verbose_name='Основное изображение')),
                ('like', models.IntegerField(default=0, help_text='Общее количество лайков', verbose_name='Лайки')),
                ('click', models.IntegerField(default=0, help_text='Общее количество кликов', verbose_name='Клики')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('categories', mptt.fields.TreeManyToManyField(blank=True, related_name='posts_cat', to='step_drawing.CategoryStepDrawingModel', verbose_name='Категории')),
                ('main_category', mptt.fields.TreeForeignKey(help_text='Используется для хлебных крошек', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_main', to='step_drawing.CategoryStepDrawingModel', verbose_name='Основная категория')),
                ('wishlist', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Запись пошаговое рисование',
                'verbose_name_plural': 'Записи пошаговое рисование',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ImagesPostDrawingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0, verbose_name='Шаг/Этап')),
                ('text1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст 1')),
                ('text2', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст 2')),
                ('text3', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст 3')),
                ('image1', models.FileField(blank=True, null=True, upload_to=step_drawing.models.images_path_post, verbose_name='Изображение 1')),
                ('image2', models.FileField(blank=True, null=True, upload_to=step_drawing.models.images_path_post, verbose_name='Изображение 2')),
                ('image3', models.FileField(blank=True, null=True, upload_to=step_drawing.models.images_path_post, verbose_name='Изображение 3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='step_drawing.PostStepDrawingModel')),
            ],
            options={
                'verbose_name': 'Изображение для постов пошагового рисования',
                'verbose_name_plural': 'Изображения для постов пошагового рисования',
                'ordering': ['position'],
            },
        ),
    ]
