# Generated by Django 5.2.1

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos', verbose_name='фото профиля'),
        ),
    ]
