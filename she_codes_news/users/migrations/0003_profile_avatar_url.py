# Generated by Django 4.0.1 on 2022-02-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(default='https://picsum.photos/600'),
        ),
    ]
