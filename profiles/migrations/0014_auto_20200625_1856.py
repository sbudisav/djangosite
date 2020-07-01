# Generated by Django 3.0.5 on 2020-06-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20200515_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplant',
            name='userplant_image',
            field=models.ImageField(blank=True, upload_to='userplant_images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_profile.jpg', upload_to='profile_images'),
        ),
    ]
