# Generated by Django 3.0.2 on 2020-04-19 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('step_drawing', '0005_auto_20200418_1658'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categorystepdrawingmodel',
            table='step_category',
        ),
        migrations.AlterModelTable(
            name='imagespostdrawingmodel',
            table='step_images',
        ),
        migrations.AlterModelTable(
            name='poststepdrawingmodel',
            table='step_posts',
        ),
        migrations.AlterModelTable(
            name='videopostmodel',
            table='step_videos',
        ),
    ]
