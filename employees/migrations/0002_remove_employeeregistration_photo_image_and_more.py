# Generated by Django 4.0.2 on 2022-03-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeregistration',
            name='photo_image',
        ),
        migrations.AddField(
            model_name='employeeregistration',
            name='_photo',
            field=models.TextField(blank=True, db_column='photo_image'),
        ),
    ]
