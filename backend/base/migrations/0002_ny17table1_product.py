# Generated by Django 4.0.1 on 2022-02-02 01:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ny17Table1',
            fields=[
                ('tmstamp', models.DateTimeField(db_column='TmStamp', primary_key=True, serialize=False)),
                ('recnum', models.BigIntegerField(db_column='RecNum')),
                ('laser_18_avg', models.FloatField(blank=True, db_column='laser_18_Avg', null=True)),
                ('laser_19_avg', models.FloatField(blank=True, db_column='laser_19_Avg', null=True)),
                ('laser_29_avg', models.FloatField(blank=True, db_column='laser_29_Avg', null=True)),
                ('laser_40_avg', models.FloatField(blank=True, db_column='laser_40_Avg', null=True)),
                ('laser_18in_avg', models.FloatField(blank=True, db_column='laser_18in_Avg', null=True)),
                ('laser_19in_avg', models.FloatField(blank=True, db_column='laser_19in_Avg', null=True)),
                ('laser_29in_avg', models.FloatField(blank=True, db_column='laser_29in_Avg', null=True)),
                ('laser_40in_avg', models.FloatField(blank=True, db_column='laser_40in_Avg', null=True)),
                ('temp_18_avg', models.FloatField(blank=True, db_column='temp_18_Avg', null=True)),
                ('temp_19_avg', models.FloatField(blank=True, db_column='temp_19_Avg', null=True)),
                ('temp_29_avg', models.FloatField(blank=True, db_column='temp_29_Avg', null=True)),
                ('temp_40_avg', models.FloatField(blank=True, db_column='temp_40_Avg', null=True)),
            ],
            options={
                'db_table': 'NY17_Table1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('countInStock', models.IntegerField(blank=True, default=0, null=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
