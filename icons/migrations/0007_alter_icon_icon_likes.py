# Generated by Django 4.2.1 on 2023-07-15 22:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('icons', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='icon_likes',
            field=models.ManyToManyField(blank=True, related_name='icon_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
