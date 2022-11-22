# Generated by Django 4.0.7 on 2022-11-22 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_salary_style'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dismissal_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='start_date_of_work',
        ),
        migrations.AddField(
            model_name='user',
            name='contract_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
