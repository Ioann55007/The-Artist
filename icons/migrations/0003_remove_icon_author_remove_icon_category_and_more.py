# Generated by Django 4.2.1 on 2023-07-15 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icons', '0002_rename_likes_icon_icon_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='icon',
            name='author',
        ),
        migrations.RemoveField(
            model_name='icon',
            name='category',
        ),
        migrations.RemoveField(
            model_name='icon',
            name='icon_likes',
        ),
        migrations.RemoveField(
            model_name='icon',
            name='viewers',
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='viewer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Icon',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Viewer',
        ),
    ]
