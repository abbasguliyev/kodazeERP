# Generated by Django 3.2.12 on 2022-09-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0005_auto_20220916_1444'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='taskmanager',
            index=models.Index(fields=['employee', 'position', 'status'], name='task_manage_employe_557437_idx'),
        ),
    ]
