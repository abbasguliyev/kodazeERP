# Generated by Django 3.2.12 on 2022-09-07 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
        ('company', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KreditorPrim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prim_faizi', models.PositiveBigIntegerField(blank=True, default=0)),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_kreditorprim', 'Mövcud kreditor primlərə baxa bilər'), ('add_kreditorprim', 'Kreditor prim əlavə edə bilər'), ('change_kreditorprim', 'Kreditor prim məlumatlarını yeniləyə bilər'), ('delete_kreditorprim', 'Kreditor prim silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='OfficeLeaderPrim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis_meblegi', models.FloatField(blank=True, default=0, null=True)),
                ('ofise_gore_prim', models.FloatField(blank=True, default=0)),
                ('fix_maas', models.FloatField(blank=True, default=0)),
                ('mehsul', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.mehsullar')),
                ('prim_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.iscistatus')),
                ('vezife', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.vezifeler')),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_officeleaderprim', 'Mövcud office leader primlərə baxa bilər'), ('add_officeleaderprim', 'Office Leader prim əlavə edə bilər'), ('change_officeleaderprim', 'Office Leader prim məlumatlarını yeniləyə bilər'), ('delete_officeleaderprim', 'Office Leader prim silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Menecer2Prim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis_meblegi', models.FloatField(blank=True, default=0, null=True)),
                ('satis0', models.FloatField(blank=True, default=0)),
                ('satis1_8', models.FloatField(blank=True, default=0)),
                ('satis9_14', models.FloatField(blank=True, default=0)),
                ('satis15p', models.FloatField(blank=True, default=0)),
                ('satis20p', models.FloatField(blank=True, default=0)),
                ('komandaya_gore_prim', models.FloatField(blank=True, default=0)),
                ('ofise_gore_prim', models.FloatField(blank=True, default=0)),
                ('fix_maas', models.FloatField(blank=True, default=0)),
                ('mehsul', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.mehsullar')),
                ('prim_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.iscistatus')),
                ('vezife', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.vezifeler')),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_menecer2prim', 'Mövcud menecer2 primlərə baxa bilər'), ('add_menecer2prim', 'Menecer2 prim əlavə edə bilər'), ('change_menecer2prim', 'Menecer2 prim məlumatlarını yeniləyə bilər'), ('delete_menecer2prim', 'Menecer2 prim silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Menecer1PrimNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis_meblegi', models.FloatField(blank=True, default=0, null=True)),
                ('negd', models.FloatField(blank=True, default=0)),
                ('kredit_4_12', models.FloatField(blank=True, default=0)),
                ('kredit_13_18', models.FloatField(blank=True, default=0)),
                ('kredit_19_24', models.FloatField(blank=True, default=0)),
                ('mehsul', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.mehsullar')),
                ('prim_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.iscistatus')),
                ('vezife', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.vezifeler')),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_menecer1primnew', 'Mövcud menecer1 primlərə baxa bilər'), ('add_menecer1primnew', 'Menecer1 prim əlavə edə bilər'), ('change_menecer1primnew', 'Menecer1 prim məlumatlarını yeniləyə bilər'), ('delete_menecer1primnew', 'Menecer1 prim silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Menecer1Prim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis_meblegi', models.FloatField(blank=True, default=0, null=True)),
                ('odenis_uslubu', models.CharField(choices=[('KREDİT', 'KREDİT'), ('NƏĞD', 'NƏĞD')], default='NƏĞD', max_length=20)),
                ('komandaya_gore_prim', models.FloatField(blank=True, default=0)),
                ('fix_maas', models.FloatField(blank=True, default=0)),
                ('mehsul', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.mehsullar')),
                ('prim_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.iscistatus')),
                ('vezife', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.vezifeler')),
            ],
            options={
                'ordering': ('pk',),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='MaasOde',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(blank=True, default=0)),
                ('qeyd', models.TextField(blank=True, default='')),
                ('odeme_tarixi', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('isci', models.ManyToManyField(related_name='maas_ode', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_maasode', 'Mövcud maaş ödəmələrinə baxa bilər'), ('add_maasode', 'Maaş ödəmə əlavə edə bilər'), ('change_maasode', 'Maaş ödəmə məlumatlarını yeniləyə bilər'), ('delete_maasode', 'Maaş ödəmə silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='MaasGoruntuleme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis_sayi', models.PositiveBigIntegerField(blank=True, default=0)),
                ('satis_meblegi', models.FloatField(blank=True, default=0)),
                ('yekun_maas', models.FloatField(blank=True, default=0)),
                ('tarix', models.DateField(blank=True, null=True)),
                ('odendi', models.BooleanField(default=False)),
                ('isci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isci_maas_goruntuleme', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_maasgoruntuleme', 'Mövcud maaş cədvəllərinə baxa bilər'), ('add_maasgoruntuleme', 'Maaş cədvəli əlavə edə bilər'), ('change_maasgoruntuleme', 'Maaş cədvəlinin məlumatlarını yeniləyə bilər'), ('delete_maasgoruntuleme', 'Maaş cədvəlini silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Kesinti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(blank=True, default=0)),
                ('qeyd', models.TextField(blank=True, default='')),
                ('kesinti_tarixi', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('isci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isci_kesinti', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_kesinti', 'Mövcud kəsintilərə baxa bilər'), ('add_kesinti', 'Kəsinti əlavə edə bilər'), ('change_kesinti', 'Kəsinti məlumatlarını yeniləyə bilər'), ('delete_kesinti', 'Kəsinti silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='GroupLeaderPrimNew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis_meblegi', models.FloatField(blank=True, default=0, null=True)),
                ('negd', models.FloatField(blank=True, default=0)),
                ('kredit_4_12', models.FloatField(blank=True, default=0)),
                ('kredit_13_18', models.FloatField(blank=True, default=0)),
                ('kredit_19_24', models.FloatField(blank=True, default=0)),
                ('mehsul', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.mehsullar')),
                ('prim_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.iscistatus')),
                ('vezife', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.vezifeler')),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_group_leaderprimnew', 'Mövcud group_leader primlərə baxa bilər'), ('add_group_leaderprimnew', 'GroupLeader prim əlavə edə bilər'), ('change_group_leaderprimnew', 'GroupLeader prim məlumatlarını yeniləyə bilər'), ('delete_group_leaderprimnew', 'GroupLeader prim silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='GroupLeaderPrim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satis_meblegi', models.FloatField(blank=True, default=0, null=True)),
                ('odenis_uslubu', models.CharField(choices=[('KREDİT', 'KREDİT'), ('NƏĞD', 'NƏĞD')], default='NƏĞD', max_length=20)),
                ('komandaya_gore_prim', models.FloatField(blank=True, default=0)),
                ('fix_maas', models.FloatField(blank=True, default=0)),
                ('mehsul', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.mehsullar')),
                ('prim_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.iscistatus')),
                ('vezife', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.vezifeler')),
            ],
            options={
                'ordering': ('pk',),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(blank=True, default=0)),
                ('qeyd', models.TextField(blank=True, default='')),
                ('bonus_tarixi', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('isci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isci_bonus', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_bonus', 'Mövcud bonuslara baxa bilər'), ('add_bonus', 'Bonus əlavə edə bilər'), ('change_bonus', 'Bonus məlumatlarını yeniləyə bilər'), ('delete_bonus', 'Bonus silə bilər')),
                'default_permissions': [],
            },
        ),
        migrations.CreateModel(
            name='Avans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mebleg', models.FloatField(blank=True, default=0)),
                ('yarim_ay_emek_haqqi', models.PositiveBigIntegerField(blank=True, default=0)),
                ('qeyd', models.TextField(blank=True, default='')),
                ('avans_tarixi', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('isci', models.ManyToManyField(related_name='isci_avans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
                'permissions': (('view_avans', 'Mövcud avanslara baxa bilər'), ('add_avans', 'Avans əlavə edə bilər'), ('change_avans', 'Avans məlumatlarını yeniləyə bilər'), ('delete_avans', 'Avans silə bilər')),
                'default_permissions': [],
            },
        ),
    ]
