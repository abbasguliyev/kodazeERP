# Generated by Django 3.2.12 on 2022-07-29 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('ofis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofis_anbar', to='company.ofis')),
                ('shirket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shirket_anbar', to='company.shirket')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Stok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('say', models.IntegerField(default=0)),
                ('anbar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='warehouse.anbar')),
                ('mehsul', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.mehsullar')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Emeliyyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mehsul_ve_sayi', models.CharField(blank=True, max_length=500, null=True)),
                ('qeyd', models.TextField(blank=True, default='', null=True)),
                ('emeliyyat_tarixi', models.DateTimeField(auto_now_add=True, null=True)),
                ('gonderen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gonderen', to='warehouse.anbar')),
                ('qebul_eden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qebul_eden', to='warehouse.anbar')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='AnbarQeydler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mehsul_ve_sayi', models.CharField(blank=True, max_length=250, null=True)),
                ('qeyd', models.TextField()),
                ('yerine_yetirildi', models.BooleanField(default=False)),
                ('gonderilme_tarixi', models.DateField(auto_now_add=True)),
                ('anbar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anbar_qeyd', to='warehouse.anbar')),
                ('gonderen_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anbar_sorgu', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]
