# Generated by Django 4.0.1 on 2022-02-12 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsstory_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='category',
            field=models.CharField(choices=[('general', 'GENERAL'), ('cats', 'CATS'), ('misc', 'MISC'), ('dogs', 'DOGS'), ('coding', 'CODING')], default='general', max_length=10),
        ),
        migrations.AddField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(default='https://picsum.photos/600'),
        ),
    ]