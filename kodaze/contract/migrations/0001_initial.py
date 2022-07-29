# Generated by Django 3.2.12 on 2022-07-29 12:19

import core.image_validator
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('company', '0001_initial'),
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Muqavile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mehsul_sayi', models.PositiveIntegerField(blank=True, default=1)),
                ('muqavile_umumi_mebleg', models.FloatField(blank=True, default=0)),
                ('elektron_imza', models.ImageField(blank=True, null=True, upload_to='media/muqavile/%Y/%m/%d/', validators=[core.image_validator.file_size, django.core.validators.FileExtensionValidator(['png', 'jpeg', 'jpg'])])),
                ('muqavile_tarixi', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('muqavile_imzalanma_tarixi', models.DateField(auto_now_add=True, null=True)),
                ('qaliq_borc', models.FloatField(blank=True, default=0)),
                ('is_sokuntu', models.BooleanField(default=False)),
                ('odenis_uslubu', models.CharField(choices=[('NƏĞD', 'NƏĞD'), ('KREDİT', 'KREDİT'), ('İKİ DƏFƏYƏ NƏĞD', 'İKİ DƏFƏYƏ NƏĞD')], default='NƏĞD', max_length=20)),
                ('negd_odenis_1', models.FloatField(blank=True, default=0)),
                ('negd_odenis_2', models.FloatField(blank=True, default=0)),
                ('negd_odenis_1_tarix', models.DateField(blank=True, null=True)),
                ('negd_odenis_2_tarix', models.DateField(blank=True, null=True)),
                ('yeni_qrafik_mebleg', models.FloatField(blank=True, default=0)),
                ('yeni_qrafik_status', models.CharField(blank=True, choices=[('YENİ QRAFİK', 'YENİ QRAFİK')], default=None, max_length=50, null=True)),
                ('deyisilmis_mehsul_status', models.CharField(blank=True, choices=[('DƏYİŞİLMİŞ MƏHSUL', 'DƏYİŞİLMİŞ MƏHSUL')], default=None, max_length=50, null=True)),
                ('negd_odenis_1_status', models.CharField(choices=[('YOXDUR', 'YOXDUR'), ('BİTMİŞ', 'BİTMİŞ'), ('DAVAM EDƏN', 'DAVAM EDƏN')], default='YOXDUR', max_length=20)),
                ('negd_odenis_2_status', models.CharField(choices=[('YOXDUR', 'YOXDUR'), ('BİTMİŞ', 'BİTMİŞ'), ('DAVAM EDƏN', 'DAVAM EDƏN')], default='YOXDUR', max_length=20)),
                ('muqavile_status', models.CharField(choices=[('DAVAM EDƏN', 'DAVAM EDƏN'), ('BİTMİŞ', 'BİTMİŞ'), ('DÜŞƏN', 'DÜŞƏN')], default='DAVAM EDƏN', max_length=20)),
                ('kredit_muddeti', models.IntegerField(blank=True, default=0)),
                ('ilkin_odenis', models.FloatField(blank=True, default=0)),
                ('ilkin_odenis_qaliq', models.FloatField(blank=True, default=0)),
                ('ilkin_odenis_tarixi', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('ilkin_odenis_qaliq_tarixi', models.DateField(blank=True, null=True)),
                ('ilkin_odenis_status', models.CharField(choices=[('YOXDUR', 'YOXDUR'), ('BİTMİŞ', 'BİTMİŞ'), ('DAVAM EDƏN', 'DAVAM EDƏN')], default='YOXDUR', max_length=20)),
                ('qaliq_ilkin_odenis_status', models.CharField(choices=[('YOXDUR', 'YOXDUR'), ('BİTMİŞ', 'BİTMİŞ'), ('DAVAM EDƏN', 'DAVAM EDƏN')], default='YOXDUR', max_length=20)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='media/media/muqavile_doc/%Y/%m/%d/', validators=[core.image_validator.file_size, django.core.validators.FileExtensionValidator(['pdf'])])),
                ('pdf_elave', models.FileField(blank=True, null=True, upload_to='media/media/muqavile_doc/%Y/%m/%d/', validators=[core.image_validator.file_size, django.core.validators.FileExtensionValidator(['pdf'])])),
                ('dusme_tarixi', models.DateField(blank=True, null=True)),
                ('kompensasiya_medaxil', models.FloatField(blank=True, default=0, null=True)),
                ('kompensasiya_mexaric', models.FloatField(blank=True, default=0, null=True)),
                ('borc_baglandi', models.BooleanField(blank=True, default=False)),
                ('canvesser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='canvesser', to=settings.AUTH_USER_MODEL)),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dealer', to=settings.AUTH_USER_MODEL)),
                ('mehsul', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mehsul_muqavile', to='product.mehsullar')),
                ('musteri', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='musteri_muqavile', to='account.musteri')),
                ('ofis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muqavile', to='company.ofis')),
                ('shirket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muqavile', to='company.shirket')),
                ('shobe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='muqavile', to='company.shobe')),
                ('vanleader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vanleader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='OdemeTarix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ay_no', models.PositiveIntegerField(default=1)),
                ('tarix', models.DateField(blank=True, default=False, null=True)),
                ('qiymet', models.FloatField(blank=True, default=0)),
                ('odenme_status', models.CharField(choices=[('ÖDƏNMƏYƏN', 'ÖDƏNMƏYƏN'), ('ÖDƏNƏN', 'ÖDƏNƏN')], default='ÖDƏNMƏYƏN', max_length=30)),
                ('sertli_odeme_status', models.CharField(blank=True, choices=[('BURAXILMIŞ AY', 'BURAXILMIŞ AY'), ('NATAMAM AY', 'NATAMAM AY'), ('RAZILAŞDIRILMIŞ AZ ÖDƏMƏ', 'RAZILAŞDIRILMIŞ AZ ÖDƏMƏ'), ('ARTIQ ÖDƏMƏ', 'ARTIQ ÖDƏMƏ'), ('SON AYIN BÖLÜNMƏSİ', 'SON AYIN BÖLÜNMƏSİ')], default=None, max_length=50, null=True)),
                ('borcu_bagla_status', models.CharField(blank=True, choices=[('BORCU BAĞLA', 'BORCU BAĞLA')], default=None, max_length=30, null=True)),
                ('gecikdirme_status', models.CharField(blank=True, choices=[('GECİKDİRMƏ', 'GECİKDİRMƏ')], default=None, max_length=30, null=True)),
                ('buraxilmis_ay_alt_status', models.CharField(blank=True, choices=[('SIFIR NÖVBƏTİ AY', 'SIFIR NÖVBƏTİ AY'), ('SIFIR SONUNCU AY', 'SIFIR SONUNCU AY'), ('SIFIR DİGƏR AYLAR', 'SIFIR DİGƏR AYLAR')], default=None, max_length=20, null=True)),
                ('natamam_ay_alt_status', models.CharField(blank=True, choices=[('NATAMAM NÖVBƏTİ AY', 'NATAMAM NÖVBƏTİ AY'), ('NATAMAM SONUNCU AY', 'NATAMAM SONUNCU AY'), ('NATAMAM DİGƏR AYLAR', 'NATAMAM DİGƏR AYLAR')], default=None, max_length=20, null=True)),
                ('artiq_odeme_alt_status', models.CharField(blank=True, choices=[('ARTIQ BİR AY', 'ARTIQ BİR AY'), ('ARTIQ BÜTÜN AYLAR', 'ARTIQ BÜTÜN AYLAR')], default=None, max_length=20, null=True)),
                ('sonuncu_ay', models.BooleanField(default=False)),
                ('qeyd', models.TextField(blank=True, default='')),
                ('muqavile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='odeme_tarixi', to='contract.muqavile')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='MuqavileKreditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kreditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='muqavile_kreditor', to=settings.AUTH_USER_MODEL)),
                ('muqavile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kreditor', to='contract.muqavile')),
            ],
        ),
        migrations.CreateModel(
            name='MuqavileHediyye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('say', models.PositiveBigIntegerField(default=1)),
                ('hediyye_tarixi', models.DateField(auto_now_add=True, null=True)),
                ('mehsul', models.ManyToManyField(related_name='mehsul_hediyye', to='product.Mehsullar')),
                ('muqavile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='muqavile_hediyye', to='contract.muqavile')),
                ('ofis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ofis_muqavile_hediyye', to='company.ofis')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Deyisim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odenis_uslubu', models.CharField(choices=[('NƏĞD', 'NƏĞD'), ('KREDİT', 'KREDİT')], default='KREDİT', max_length=100)),
                ('kredit_muddeti', models.IntegerField(blank=True, default=0)),
                ('kohne_muqavile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deyisim', to='contract.muqavile')),
                ('mehsul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deyisim', to='product.mehsullar')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='DemoSatis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('created_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('sale_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
    ]
