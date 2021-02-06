# Generated by Django 3.0.2 on 2020-04-15 13:05

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
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
                ('image', models.FileField(blank=True, help_text='Отображается в категории', null=True, upload_to=posts.models.image_path_category, verbose_name='Основное изображение')),
                ('image_menu', models.FileField(blank=True, help_text='Иконка в меню', null=True, upload_to=posts.models.image_menu_path_category, verbose_name='Картинка в меню')),
                ('show_main', models.BooleanField(default=False, verbose_name='Отображать на главной или нет')),
                ('image_main', models.FileField(blank=True, help_text='Отображается на главной', null=True, upload_to=posts.models.image_main_path_category, verbose_name='Картинка на главной')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(default=0, verbose_name='Позиция')),
                ('enabled', models.BooleanField(choices=[(True, 'Опубликовано'), (False, 'Не опубликовано')], default=False, help_text='Отображать/неотображать пост', verbose_name='Опубликовано')),
                ('name', models.CharField(help_text='Название поста', max_length=250, unique=True, verbose_name='h1')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Url(slug)')),
                ('title', models.CharField(default='Картинка для срисовки', max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(help_text='Ожидается изображение 800х800 jpeg', upload_to=posts.models.image_path_post, verbose_name='Изображение')),
                ('like', models.IntegerField(default=0, help_text='Общее количество лайков', verbose_name='Лайки')),
                ('click', models.IntegerField(default=0, help_text='Общее количество кликов', verbose_name='Клики')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('categories', mptt.fields.TreeManyToManyField(blank=True, related_name='posts_cat', to='posts.Category', verbose_name='Категории')),
                ('main_category', mptt.fields.TreeForeignKey(help_text='Используется для хлебных крошек', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_main', to='posts.Category', verbose_name='Основная категория')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['-created_at'],
            },
        ),
    ]
