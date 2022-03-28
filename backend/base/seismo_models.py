#####################################
#C:\Users\georg\Dropbox\udemy\django_react\backend
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HistoBe13501(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be13501'


class HistoBe13658(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be13658'


class HistoBe13833(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be13833'


class HistoBe13835(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be13835'


class HistoBe13836(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be13836'


class HistoBe13868(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be13868'


class HistoBe14054(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be14054'


class HistoBe19849(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_be19849'


class HistoMp12625(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_mp12625'


class HistoMp12897(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_mp12897'


class HistoUm10307(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um10307'


class HistoUm10308(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um10308'


class HistoUm10374(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um10374'


class HistoUm12302(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um12302'


class HistoUm12319(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um12319'


class HistoUm12616(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um12616'


class HistoUm14474(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um14474'


class HistoUm16265(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um16265'


class HistoUm16427(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um16427'


class HistoUm16428(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um16428'


class HistoUm16429(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um16429'


class HistoUm16433(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um16433'


class HistoUm16435(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um16435'


class HistoUm16455(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um16455'


class HistoUm6377(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um6377'


class HistoUm6378(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um6378'


class HistoUm6379(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um6379'


class HistoUm6380(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_um6380'


class SeismoHistoFiles(models.Model):
    filename = models.CharField(primary_key=True, max_length=100)
    filetype = models.CharField(max_length=10, blank=True, null=True)
    datetime_logged = models.DateTimeField(blank=True, null=True)
    datetime_started = models.DateTimeField(blank=True, null=True)
    unit_id = models.TextField(blank=True, null=True)
    commits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seismo_histo_files'


class SeismoWaveforms(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    seismo_id = models.TextField(blank=True, null=True)
    project_id = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    tran_pk_ppv = models.FloatField(blank=True, null=True)
    vert_pk_ppv = models.FloatField(blank=True, null=True)
    long_pk_ppv = models.FloatField(blank=True, null=True)
    tran = models.TextField(blank=True, null=True)
    vert = models.TextField(blank=True, null=True)
    long = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seismo_waveforms'

class HistoMp12626Slm(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    tran_ppv = models.FloatField(blank=True, null=True)
    tran_hz = models.FloatField(blank=True, null=True)
    vert_ppv = models.FloatField(blank=True, null=True)
    vert_hz = models.FloatField(blank=True, null=True)
    long_ppv = models.FloatField(blank=True, null=True)
    long_hz = models.FloatField(blank=True, null=True)
    geophone_ppv = models.FloatField(blank=True, null=True)
    lmax = models.FloatField(blank=True, null=True)
    lmin = models.FloatField(blank=True, null=True)
    l10 = models.FloatField(blank=True, null=True)
    l90 = models.FloatField(blank=True, null=True)
    leq = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'histo_mp12626_slm'