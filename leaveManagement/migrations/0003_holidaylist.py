# Generated by Django 4.0.2 on 2022-03-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveManagement', '0002_rename_values_leavetype_leave_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolidayList',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('display_name', models.TextField(max_length=200)),
            ],
        ),
    ]
