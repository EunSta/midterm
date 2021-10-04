# Generated by Django 3.2.3 on 2021-07-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Car_Model', max_length=255, null=True)),
                ('min_fe', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Min_FE', max_length=255, null=True)),
                ('max_fe', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Max_FE', max_length=255, null=True)),
                ('min_pri', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Min_Pri', max_length=255, null=True)),
                ('max_pri', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Max_Pri', max_length=255, null=True)),
                ('car_type', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Car_Type', max_length=255, null=True)),
                ('mcar_infoproducts1aker', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Mcar_infoproducts1aker', max_length=50, null=True)),
                ('rdate', models.DateField(blank=True, db_column='Rdate', null=True)),
                ('exterior', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Exterior', max_length=50, null=True)),
                ('ol', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='OL', max_length=50, null=True)),
                ('ow', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='OW', max_length=50, null=True)),
                ('oh', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='OH', max_length=50, null=True)),
                ('wb', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='WB', max_length=50, null=True)),
                ('uvw', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='UVW', max_length=50, null=True)),
                ('limn', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='LimN', max_length=50, null=True)),
                ('ftc', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='FTC', max_length=50, null=True)),
                ('tc', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='TC', max_length=50, null=True)),
                ('eng', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Eng', max_length=50, null=True)),
                ('dm', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='DM', max_length=50, null=True)),
                ('maxp', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='MAXP', max_length=50, null=True)),
                ('maxor', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='MAXOR', max_length=50, null=True)),
                ('maxt', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='MAXT', max_length=50, null=True)),
                ('maxtr', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='MAXTR', max_length=50, null=True)),
                ('engposi', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='EngPosi', max_length=50, null=True)),
                ('maxspeed', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='MAXSPEED', max_length=50, null=True)),
                ('battery', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Battery', max_length=50, null=True)),
                ('battery_tyep', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Battery_Tyep', max_length=50, null=True)),
                ('dt', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='DT', max_length=50, null=True)),
                ('tm', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Tm', max_length=50, null=True)),
                ('ps', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='PS', max_length=50, null=True)),
                ('st', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='St', max_length=50, null=True)),
                ('fw', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='FW', max_length=50, null=True)),
                ('rw', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='RW', max_length=50, null=True)),
                ('fts', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='FTS', max_length=50, null=True)),
                ('rts', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='RTS', max_length=50, null=True)),
                ('fs', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='FS', max_length=50, null=True)),
                ('rs', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='RS', max_length=50, null=True)),
                ('fuel', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='Fuel', max_length=50, null=True)),
                ('cde', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='CDE', max_length=50, null=True)),
                ('fcr', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='FCR', max_length=50, null=True)),
                ('fer', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='FER', max_length=50, null=True)),
                ('fcm', models.CharField(blank=True, db_collation='euckr_korean_ci', db_column='FCM', max_length=50, null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
    ]