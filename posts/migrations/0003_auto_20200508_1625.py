# Generated by Django 3.0.5 on 2020-05-08 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='post_image',
        ),
    ]