# Generated by Django 4.0.7 on 2022-10-12 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_alter_contractcreditor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractgift',
            name='gift_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
