# Generated by Django 3.0.5 on 2020-05-06 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0005_auto_20200505_0246'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PublicProfile', 
            new_name='UserProfile'),

        migrations.AddField(
            model_name='UserProfile',
            name='about',
            field=(models.CharField(max_length=600, default=''))
        ),
        migrations.AddField(
            model_name='UserProfile',
            name='zipcode',
            field=(models.CharField(max_length=5, default=''))
        ),
        migrations.AddField(
            model_name='UserProfile',
            name='requires_comment_validation',
            field=(models.BooleanField(default=False))
        ),
        migrations.DeleteModel(
            name='PrivateProfile',
        ),
    ]
