# Generated by Django 4.0.7 on 2022-11-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_user_holding_remove_user_section_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='salary_style',
            field=models.CharField(choices=[('Fix+Kommissiya', 'Fix+Kommissiya'), ('Kommissiya', 'Kommissiya'), ('Fix', 'Fix')], default='Fix', max_length=50),
        ),
    ]
