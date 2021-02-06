# Generated by Django 3.0.2 on 2020-04-18 05:39

import ckeditor.fields
from django.db import migrations, models
import step_drawing.models


class Migration(migrations.Migration):

    dependencies = [
        ('step_drawing', '0002_poststepdrawingmodel_execution_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagespostdrawingmodel',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='imagespostdrawingmodel',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='imagespostdrawingmodel',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='imagespostdrawingmodel',
            name='text1',
        ),
        migrations.RemoveField(
            model_name='imagespostdrawingmodel',
            name='text2',
        ),
        migrations.RemoveField(
            model_name='imagespostdrawingmodel',
            name='text3',
        ),
        migrations.AddField(
            model_name='imagespostdrawingmodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=step_drawing.models.images_path_post, verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='imagespostdrawingmodel',
            name='text_down',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст внизу'),
        ),
        migrations.AddField(
            model_name='imagespostdrawingmodel',
            name='text_up',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст сверху'),
        ),
        migrations.AddField(
            model_name='poststepdrawingmodel',
            name='show_main',
            field=models.BooleanField(default=False, verbose_name='Отображать на главной или нет'),
        ),
        migrations.AlterField(
            model_name='categorystepdrawingmodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=step_drawing.models.image_path_category, verbose_name='Какое-то изображение'),
        ),
        migrations.AlterField(
            model_name='poststepdrawingmodel',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]