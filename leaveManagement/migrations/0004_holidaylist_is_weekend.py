# Generated by Django 4.0.2 on 2022-03-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveManagement', '0003_holidaylist'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidaylist',
            name='is_weekend',
            field=models.BooleanField(default=False),
        ),
    ]