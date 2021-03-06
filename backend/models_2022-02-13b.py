# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class 420WashTable1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    sevolt_avg_1 = models.FloatField(db_column='SEVolt_Avg_1', blank=True, null=True)  # Field name made lowercase.
    sevolt_avg_2 = models.FloatField(db_column='SEVolt_Avg_2', blank=True, null=True)  # Field name made lowercase.
    sevolt_avg_3 = models.FloatField(db_column='SEVolt_Avg_3', blank=True, null=True)  # Field name made lowercase.
    sevolt_avg_4 = models.FloatField(db_column='SEVolt_Avg_4', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg = models.FloatField(db_column='DiffVolt_Avg', blank=True, null=True)  # Field name made lowercase.
    tilt1_avg = models.FloatField(db_column='Tilt1_Avg', blank=True, null=True)  # Field name made lowercase.
    tilt2_avg = models.FloatField(db_column='Tilt2_Avg', blank=True, null=True)  # Field name made lowercase.
    temptilt1_avg = models.FloatField(db_column='TempTilt1_Avg', blank=True, null=True)  # Field name made lowercase.
    temptilt2_avg = models.FloatField(db_column='TempTilt2_Avg', blank=True, null=True)  # Field name made lowercase.
    disp_avg = models.FloatField(db_column='Disp_Avg', blank=True, null=True)  # Field name made lowercase.
    disp2_avg = models.FloatField(db_column='Disp2_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '420Wash_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr1000FtlaudLiftevent(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    measure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CR1000_ftlaud_LiftEvent'
        unique_together = (('tmstamp', 'recnum'),)


class Cr1000FtlaudMonitor(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    measure_avg = models.FloatField(db_column='measure_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp = models.FloatField(db_column='PTemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR1000_ftlaud_Monitor'
        unique_together = (('tmstamp', 'recnum'),)


class Cr1000FtlaudEvent(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    measure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CR1000_ftlaud_event'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series1Cpistatus(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    busload = models.FloatField(db_column='BusLoad', blank=True, null=True)  # Field name made lowercase.
    modulereportcount = models.IntegerField(db_column='ModuleReportCount', blank=True, null=True)  # Field name made lowercase.
    activemodules = models.IntegerField(db_column='ActiveModules', blank=True, null=True)  # Field name made lowercase.
    bufferr = models.IntegerField(db_column='BuffErr', blank=True, null=True)  # Field name made lowercase.
    rxerrmax = models.IntegerField(db_column='RxErrMax', blank=True, null=True)  # Field name made lowercase.
    txerrmax = models.IntegerField(db_column='TxErrMax', blank=True, null=True)  # Field name made lowercase.
    frameerr = models.IntegerField(db_column='FrameErr', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_1 = models.TextField(db_column='ModuleInfo_1', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_2 = models.TextField(db_column='ModuleInfo_2', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_3 = models.TextField(db_column='ModuleInfo_3', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_4 = models.TextField(db_column='ModuleInfo_4', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_5 = models.TextField(db_column='ModuleInfo_5', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_6 = models.TextField(db_column='ModuleInfo_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_1_CPIStatus'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series1Calhist(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    caltime = models.DateTimeField(db_column='CalTime', blank=True, null=True)  # Field name made lowercase.
    coff = models.FloatField(db_column='COff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_1_CalHist'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series1Table1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    daq1_lvdt_avg = models.FloatField(db_column='DAQ1_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_1_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series1Table2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_min = models.FloatField(db_column='BattV_Min', blank=True, null=True)  # Field name made lowercase.
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.
    daq1_enc_temp_f = models.FloatField(db_column='DAQ1_Enc_Temp_F', blank=True, null=True)  # Field name made lowercase.
    daq1_temp_f_1 = models.FloatField(db_column='DAQ1_Temp_F_1', blank=True, null=True)  # Field name made lowercase.
    daq1_temp_f_2 = models.FloatField(db_column='DAQ1_Temp_F_2', blank=True, null=True)  # Field name made lowercase.
    daq1_enc_rh = models.FloatField(db_column='DAQ1_Enc_RH', blank=True, null=True)  # Field name made lowercase.
    daq1_lvdt_avg = models.FloatField(db_column='DAQ1_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.
    daq1_temp_f = models.FloatField(db_column='DAQ1_Temp_F', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_1_Table2'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series1TableHealth(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_c_avg = models.FloatField(db_column='PTemp_C_Avg', blank=True, null=True)  # Field name made lowercase.
    a12_temp_avg = models.FloatField(db_column='A12_Temp_Avg', blank=True, null=True)  # Field name made lowercase.
    a12_rh_avg = models.FloatField(db_column='A12_RH_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_1_Table_Health'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series1TableSlow(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    b12w_aux_lvdt_avg = models.FloatField(db_column='B12W_AUX_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.
    b12w_aux_temp_avg = models.FloatField(db_column='B12W_AUX_Temp_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_1_Table_Slow'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series1TableSlowArch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    b12w_aux_lvdt_avg = models.FloatField(db_column='B12W_AUX_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.
    b12w_aux_temp_avg = models.FloatField(db_column='B12W_AUX_Temp_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_1_Table_Slow_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2Cpistatus(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    busload = models.FloatField(db_column='BusLoad', blank=True, null=True)  # Field name made lowercase.
    modulereportcount = models.IntegerField(db_column='ModuleReportCount', blank=True, null=True)  # Field name made lowercase.
    activemodules = models.IntegerField(db_column='ActiveModules', blank=True, null=True)  # Field name made lowercase.
    bufferr = models.IntegerField(db_column='BuffErr', blank=True, null=True)  # Field name made lowercase.
    rxerrmax = models.IntegerField(db_column='RxErrMax', blank=True, null=True)  # Field name made lowercase.
    txerrmax = models.IntegerField(db_column='TxErrMax', blank=True, null=True)  # Field name made lowercase.
    frameerr = models.IntegerField(db_column='FrameErr', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_1 = models.TextField(db_column='ModuleInfo_1', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_2 = models.TextField(db_column='ModuleInfo_2', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_3 = models.TextField(db_column='ModuleInfo_3', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_4 = models.TextField(db_column='ModuleInfo_4', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_5 = models.TextField(db_column='ModuleInfo_5', blank=True, null=True)  # Field name made lowercase.
    moduleinfo_6 = models.TextField(db_column='ModuleInfo_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_CPIStatus'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2Calhist(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    caltime = models.DateTimeField(db_column='CalTime', blank=True, null=True)  # Field name made lowercase.
    coff = models.FloatField(db_column='COff', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_CalHist'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2Public(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv = models.FloatField(db_column='BattV', blank=True, null=True)  # Field name made lowercase.
    fcloaded = models.FloatField(db_column='FCLoaded', blank=True, null=True)  # Field name made lowercase.
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.
    daq2_enc_temp_f = models.FloatField(db_column='DAQ2_Enc_Temp_F', blank=True, null=True)  # Field name made lowercase.
    daq2_lvdt = models.FloatField(db_column='DAQ2_LVDT', blank=True, null=True)  # Field name made lowercase.
    coff = models.FloatField(db_column='COff', blank=True, null=True)  # Field name made lowercase.
    creps = models.FloatField(db_column='CReps', blank=True, null=True)  # Field name made lowercase.
    zmode = models.FloatField(db_column='ZMode', blank=True, null=True)  # Field name made lowercase.
    cindex = models.FloatField(db_column='CIndex', blank=True, null=True)  # Field name made lowercase.
    cavg = models.FloatField(db_column='CAvg', blank=True, null=True)  # Field name made lowercase.
    daq2_temp_f = models.FloatField(db_column='DAQ2_Temp_F', blank=True, null=True)  # Field name made lowercase.
    daq2_enc_rh = models.FloatField(db_column='DAQ2_Enc_RH', blank=True, null=True)  # Field name made lowercase.
    flag = models.FloatField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_Public'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2Table1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    daq2_lvdt_avg = models.FloatField(db_column='DAQ2_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2Table2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_min = models.FloatField(db_column='BattV_Min', blank=True, null=True)  # Field name made lowercase.
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.
    daq2_enc_temp_f = models.FloatField(db_column='DAQ2_Enc_Temp_F', blank=True, null=True)  # Field name made lowercase.
    daq2_temp_f_1 = models.FloatField(db_column='DAQ2_Temp_F_1', blank=True, null=True)  # Field name made lowercase.
    daq2_temp_f_2 = models.FloatField(db_column='DAQ2_Temp_F_2', blank=True, null=True)  # Field name made lowercase.
    daq2_enc_rh = models.FloatField(db_column='DAQ2_Enc_RH', blank=True, null=True)  # Field name made lowercase.
    daq2_lvdt_avg = models.FloatField(db_column='DAQ2_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.
    daq2_temp_f = models.FloatField(db_column='DAQ2_Temp_F', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_Table2'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2TableHealth(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_c_avg = models.FloatField(db_column='PTemp_C_Avg', blank=True, null=True)  # Field name made lowercase.
    a4_temp_avg = models.FloatField(db_column='A4_Temp_Avg', blank=True, null=True)  # Field name made lowercase.
    a4_rh_avg = models.FloatField(db_column='A4_RH_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_Table_Health'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2TableSlow(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    b4n_aux_lvdt_avg = models.FloatField(db_column='B4N_AUX_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_aux_temp_avg = models.FloatField(db_column='B4N_AUX_Temp_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_Table_Slow'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series2TableSlowArch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    b4n_aux_lvdt_avg = models.FloatField(db_column='B4N_AUX_LVDT_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_aux_temp_avg = models.FloatField(db_column='B4N_AUX_Temp_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_2_Table_Slow_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series3TableHealth(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_med = models.FloatField(db_column='BattV_Med', blank=True, null=True)  # Field name made lowercase.
    ptemp_c_med = models.FloatField(db_column='PTemp_C_Med', blank=True, null=True)  # Field name made lowercase.
    t12_temp_med = models.FloatField(db_column='T12_Temp_Med', blank=True, null=True)  # Field name made lowercase.
    t12_rh_med = models.FloatField(db_column='T12_RH_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_3_Table_Health'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series3TableSlow(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_12_radial_med = models.FloatField(db_column='T_12_Radial_Med', blank=True, null=True)  # Field name made lowercase.
    t_12_tangent_med = models.FloatField(db_column='T_12_Tangent_Med', blank=True, null=True)  # Field name made lowercase.
    t_12_tempf_med = models.FloatField(db_column='T_12_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_aux_t_med = models.FloatField(db_column='M12W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_aux_t_med = models.FloatField(db_column='B12W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_w_aux_med = models.FloatField(db_column='M12W_W_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_e_aux_med = models.FloatField(db_column='M12W_E_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_w_aux_med = models.FloatField(db_column='B12W_W_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_e_aux_med = models.FloatField(db_column='B12W_E_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m12e_w_aux_med = models.FloatField(db_column='M12E_W_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m12e_e_aux_med = models.FloatField(db_column='M12E_E_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b12e_w_aux_med = models.FloatField(db_column='B12E_W_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b12e_e_aux_med = models.FloatField(db_column='B12E_E_Aux_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_3_Table_Slow'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series3TableSlowLoadonly(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_12_radial_med = models.FloatField(db_column='T_12_Radial_Med', blank=True, null=True)  # Field name made lowercase.
    t_12_tangent_med = models.FloatField(db_column='T_12_Tangent_Med', blank=True, null=True)  # Field name made lowercase.
    t_12_tempf_med = models.FloatField(db_column='T_12_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_aux_t_med = models.FloatField(db_column='M12W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_aux_t_med = models.FloatField(db_column='B12W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_w_aux_static_l_med = models.FloatField(db_column='M12W_W_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_e_aux_static_l_med = models.FloatField(db_column='M12W_E_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_w_aux_static_l_med = models.FloatField(db_column='B12W_W_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_e_aux_static_l_med = models.FloatField(db_column='B12W_E_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m12e_w_aux_static_l_med = models.FloatField(db_column='M12E_W_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m12e_e_aux_static_l_med = models.FloatField(db_column='M12E_E_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b12e_w_aux_static_l_med = models.FloatField(db_column='B12E_W_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b12e_e_aux_static_l_med = models.FloatField(db_column='B12E_E_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_3_Table_Slow_LoadOnly'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series3TableSlowT(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    m12w_w_aux_t_med = models.FloatField(db_column='M12W_W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_e_aux_t_med = models.FloatField(db_column='M12W_E_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_w_aux_t_med = models.FloatField(db_column='B12W_W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_e_aux_t_med = models.FloatField(db_column='B12W_E_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m12e_w_aux_t_med = models.FloatField(db_column='M12E_W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m12e_e_aux_t_med = models.FloatField(db_column='M12E_E_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b12e_w_aux_t_med = models.FloatField(db_column='B12E_W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b12e_e_aux_t_med = models.FloatField(db_column='B12E_E_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    t_12_tempf_med = models.FloatField(db_column='T_12_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m12w_aux_t_med = models.FloatField(db_column='M12W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b12w_aux_t_med = models.FloatField(db_column='B12W_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_3_Table_Slow_T'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series3TableSlowW(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    winddir_med = models.FloatField(db_column='WindDir_Med', blank=True, null=True)  # Field name made lowercase.
    windspeed_med = models.FloatField(db_column='WindSpeed_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_3_Table_Slow_W'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series4TableHealth(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_med = models.FloatField(db_column='BattV_Med', blank=True, null=True)  # Field name made lowercase.
    ptemp_c_med = models.FloatField(db_column='PTemp_C_Med', blank=True, null=True)  # Field name made lowercase.
    t4_temp_med = models.FloatField(db_column='T4_Temp_Med', blank=True, null=True)  # Field name made lowercase.
    t4_rh_med = models.FloatField(db_column='T4_RH_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_4_Table_Health'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series4TableSlow(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_4_radial_med = models.FloatField(db_column='T_4_Radial_Med', blank=True, null=True)  # Field name made lowercase.
    t_4_tangent_med = models.FloatField(db_column='T_4_Tangent_Med', blank=True, null=True)  # Field name made lowercase.
    t_4_tempf_med = models.FloatField(db_column='T_4_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_aux_t_med = models.FloatField(db_column='M4S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_aux_t_med = models.FloatField(db_column='B4N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m4n_n_aux_med = models.FloatField(db_column='M4N_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m4n_s_aux_med = models.FloatField(db_column='M4N_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_n_aux_med = models.FloatField(db_column='B4N_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_s_aux_med = models.FloatField(db_column='B4N_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_n_aux_med = models.FloatField(db_column='M4S_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_s_aux_med = models.FloatField(db_column='M4S_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b4s_n_aux_med = models.FloatField(db_column='B4S_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b4s_s_aux_med = models.FloatField(db_column='B4S_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_4_Table_Slow'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series4TableSlowLoadonly(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_4_radial_med = models.FloatField(db_column='T_4_Radial_Med', blank=True, null=True)  # Field name made lowercase.
    t_4_tangent_med = models.FloatField(db_column='T_4_Tangent_Med', blank=True, null=True)  # Field name made lowercase.
    t_4_tempf_med = models.FloatField(db_column='T_4_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_aux_t_med = models.FloatField(db_column='M4S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_aux_t_med = models.FloatField(db_column='B4N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m4n_n_aux_static_l_med = models.FloatField(db_column='M4N_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m4n_s_aux_static_l_med = models.FloatField(db_column='M4N_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_n_aux_static_l_med = models.FloatField(db_column='B4N_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_s_aux_static_l_med = models.FloatField(db_column='B4N_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_n_aux_static_l_med = models.FloatField(db_column='M4S_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_s_aux_static_l_med = models.FloatField(db_column='M4S_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b4s_n_aux_static_l_med = models.FloatField(db_column='B4S_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b4s_s_aux_static_l_med = models.FloatField(db_column='B4S_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_4_Table_Slow_LoadOnly'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series4TableSlowLoadonlyArch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_4_radial_avg = models.FloatField(db_column='T_4_Radial_Avg', blank=True, null=True)  # Field name made lowercase.
    t_4_tangent_avg = models.FloatField(db_column='T_4_Tangent_Avg', blank=True, null=True)  # Field name made lowercase.
    t_4_tempf_avg = models.FloatField(db_column='T_4_TempF_Avg', blank=True, null=True)  # Field name made lowercase.
    m4s_aux_t_avg = models.FloatField(db_column='M4S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_aux_t_avg = models.FloatField(db_column='B4N_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m4n_n_aux_static_l_avg = models.FloatField(db_column='M4N_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    m4n_s_aux_static_l_avg = models.FloatField(db_column='M4N_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_n_aux_static_l_avg = models.FloatField(db_column='B4N_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_s_aux_static_l_avg = models.FloatField(db_column='B4N_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    m4s_n_aux_static_l_avg = models.FloatField(db_column='M4S_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    m4s_s_aux_static_l_avg = models.FloatField(db_column='M4S_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b4s_n_aux_static_l_avg = models.FloatField(db_column='B4S_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b4s_s_aux_static_l_avg = models.FloatField(db_column='B4S_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_4_Table_Slow_LoadOnly_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series4TableSlowT(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    m4n_n_aux_t_med = models.FloatField(db_column='M4N_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m4n_s_aux_t_med = models.FloatField(db_column='M4N_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_n_aux_t_med = models.FloatField(db_column='B4N_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_s_aux_t_med = models.FloatField(db_column='B4N_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_n_aux_t_med = models.FloatField(db_column='M4S_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_s_aux_t_med = models.FloatField(db_column='M4S_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b4s_n_aux_t_med = models.FloatField(db_column='B4S_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b4s_s_aux_t_med = models.FloatField(db_column='B4S_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    t_4_tempf_med = models.FloatField(db_column='T_4_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m4s_aux_t_med = models.FloatField(db_column='M4S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b4n_aux_t_med = models.FloatField(db_column='B4N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_4_Table_Slow_T'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series4TableSlowArch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_4_radial_avg = models.FloatField(db_column='T_4_Radial_Avg', blank=True, null=True)  # Field name made lowercase.
    t_4_tangent_avg = models.FloatField(db_column='T_4_Tangent_Avg', blank=True, null=True)  # Field name made lowercase.
    t_4_tempf_avg = models.FloatField(db_column='T_4_TempF_Avg', blank=True, null=True)  # Field name made lowercase.
    m4s_aux_t_avg = models.FloatField(db_column='M4S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_aux_t_avg = models.FloatField(db_column='B4N_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m4n_n_aux_avg = models.FloatField(db_column='M4N_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m4n_s_aux_avg = models.FloatField(db_column='M4N_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_n_aux_avg = models.FloatField(db_column='B4N_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b4n_s_aux_avg = models.FloatField(db_column='B4N_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m4s_n_aux_avg = models.FloatField(db_column='M4S_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m4s_s_aux_avg = models.FloatField(db_column='M4S_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b4s_n_aux_avg = models.FloatField(db_column='B4S_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b4s_s_aux_avg = models.FloatField(db_column='B4S_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_4_Table_Slow_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series5TableHealth(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_med = models.FloatField(db_column='BattV_Med', blank=True, null=True)  # Field name made lowercase.
    ptemp_c_med = models.FloatField(db_column='PTemp_C_Med', blank=True, null=True)  # Field name made lowercase.
    t8_temp_med = models.FloatField(db_column='T8_Temp_Med', blank=True, null=True)  # Field name made lowercase.
    t8_rh_med = models.FloatField(db_column='T8_RH_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_5_Table_Health'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series5TableSlow(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_8_radial_avg = models.FloatField(db_column='T_8_Radial_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_tangent_avg = models.FloatField(db_column='T_8_Tangent_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_tempf_avg = models.FloatField(db_column='T_8_TempF_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_aux_t_avg = models.FloatField(db_column='M8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_aux_t_avg = models.FloatField(db_column='B8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_s_aux_avg = models.FloatField(db_column='M8S_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_n_aux_avg = models.FloatField(db_column='M8S_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_s_aux_avg = models.FloatField(db_column='B8S_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_n_aux_avg = models.FloatField(db_column='B8S_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_s_aux_avg = models.FloatField(db_column='M8N_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_n_aux_avg = models.FloatField(db_column='M8N_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_s_aux_avg = models.FloatField(db_column='B8N_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_n_aux_avg = models.FloatField(db_column='B8N_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_radial_med = models.FloatField(db_column='T_8_Radial_Med', blank=True, null=True)  # Field name made lowercase.
    t_8_tangent_med = models.FloatField(db_column='T_8_Tangent_Med', blank=True, null=True)  # Field name made lowercase.
    t_8_tempf_med = models.FloatField(db_column='T_8_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_aux_t_med = models.FloatField(db_column='M8S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_aux_t_med = models.FloatField(db_column='B8S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_s_aux_med = models.FloatField(db_column='M8S_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_n_aux_med = models.FloatField(db_column='M8S_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_s_aux_med = models.FloatField(db_column='B8S_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_n_aux_med = models.FloatField(db_column='B8S_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m8n_s_aux_med = models.FloatField(db_column='M8N_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    m8n_n_aux_med = models.FloatField(db_column='M8N_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b8n_s_aux_med = models.FloatField(db_column='B8N_S_Aux_Med', blank=True, null=True)  # Field name made lowercase.
    b8n_n_aux_med = models.FloatField(db_column='B8N_N_Aux_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_5_Table_Slow'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series5TableSlowLoadonly(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_8_radial_med = models.FloatField(db_column='T_8_Radial_Med', blank=True, null=True)  # Field name made lowercase.
    t_8_tangent_med = models.FloatField(db_column='T_8_Tangent_Med', blank=True, null=True)  # Field name made lowercase.
    t_8_tempf_med = models.FloatField(db_column='T_8_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_aux_t_med = models.FloatField(db_column='M8S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_aux_t_med = models.FloatField(db_column='B8S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_s_aux_static_l_med = models.FloatField(db_column='M8S_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_n_aux_static_l_med = models.FloatField(db_column='M8S_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_s_aux_static_l_med = models.FloatField(db_column='B8S_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_n_aux_static_l_med = models.FloatField(db_column='B8S_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m8n_s_aux_static_l_med = models.FloatField(db_column='M8N_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    m8n_n_aux_static_l_med = models.FloatField(db_column='M8N_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b8n_s_aux_static_l_med = models.FloatField(db_column='B8N_S_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.
    b8n_n_aux_static_l_med = models.FloatField(db_column='B8N_N_Aux_Static_L_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_5_Table_Slow_LoadOnly'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series5TableSlowLoadonlyArch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_8_radial_avg = models.FloatField(db_column='T_8_Radial_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_tangent_avg = models.FloatField(db_column='T_8_Tangent_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_tempf_avg = models.FloatField(db_column='T_8_TempF_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_aux_t_avg = models.FloatField(db_column='M8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_aux_t_avg = models.FloatField(db_column='B8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_s_aux_static_l_avg = models.FloatField(db_column='M8S_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_n_aux_static_l_avg = models.FloatField(db_column='M8S_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_s_aux_static_l_avg = models.FloatField(db_column='B8S_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_n_aux_static_l_avg = models.FloatField(db_column='B8S_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_s_aux_static_l_avg = models.FloatField(db_column='M8N_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_n_aux_static_l_avg = models.FloatField(db_column='M8N_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_s_aux_static_l_avg = models.FloatField(db_column='B8N_S_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_n_aux_static_l_avg = models.FloatField(db_column='B8N_N_Aux_Static_L_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_5_Table_Slow_LoadOnly_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series5TableSlowT(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    m8s_s_aux_t_med = models.FloatField(db_column='M8S_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_n_aux_t_med = models.FloatField(db_column='M8S_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_s_aux_t_med = models.FloatField(db_column='B8S_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_n_aux_t_med = models.FloatField(db_column='B8S_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m8n_s_aux_t_med = models.FloatField(db_column='M8N_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    m8n_n_aux_t_med = models.FloatField(db_column='M8N_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b8n_s_aux_t_med = models.FloatField(db_column='B8N_S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b8n_n_aux_t_med = models.FloatField(db_column='B8N_N_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    t_8_tempf_med = models.FloatField(db_column='T_8_TempF_Med', blank=True, null=True)  # Field name made lowercase.
    m8s_aux_t_med = models.FloatField(db_column='M8S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.
    b8s_aux_t_med = models.FloatField(db_column='B8S_Aux_T_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_5_Table_Slow_T'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series5TableSlowTArch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    m8s_s_aux_t_avg = models.FloatField(db_column='M8S_S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_n_aux_t_avg = models.FloatField(db_column='M8S_N_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_s_aux_t_avg = models.FloatField(db_column='B8S_S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_n_aux_t_avg = models.FloatField(db_column='B8S_N_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_s_aux_t_avg = models.FloatField(db_column='M8N_S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_n_aux_t_avg = models.FloatField(db_column='M8N_N_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_s_aux_t_avg = models.FloatField(db_column='B8N_S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_n_aux_t_avg = models.FloatField(db_column='B8N_N_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_tempf_avg = models.FloatField(db_column='T_8_TempF_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_aux_t_avg = models.FloatField(db_column='M8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_aux_t_avg = models.FloatField(db_column='B8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_5_Table_Slow_T_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series5TableSlowArch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    t_8_radial_avg = models.FloatField(db_column='T_8_Radial_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_tangent_avg = models.FloatField(db_column='T_8_Tangent_Avg', blank=True, null=True)  # Field name made lowercase.
    t_8_tempf_avg = models.FloatField(db_column='T_8_TempF_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_aux_t_avg = models.FloatField(db_column='M8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_aux_t_avg = models.FloatField(db_column='B8S_Aux_T_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_s_aux_avg = models.FloatField(db_column='M8S_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m8s_n_aux_avg = models.FloatField(db_column='M8S_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_s_aux_avg = models.FloatField(db_column='B8S_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8s_n_aux_avg = models.FloatField(db_column='B8S_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_s_aux_avg = models.FloatField(db_column='M8N_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    m8n_n_aux_avg = models.FloatField(db_column='M8N_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_s_aux_avg = models.FloatField(db_column='B8N_S_Aux_Avg', blank=True, null=True)  # Field name made lowercase.
    b8n_n_aux_avg = models.FloatField(db_column='B8N_N_Aux_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_5_Table_Slow_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Cr6Series6Table2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_min = models.FloatField(db_column='BattV_Min', blank=True, null=True)  # Field name made lowercase.
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.
    daq6_enc_temp_f = models.FloatField(db_column='DAQ6_Enc_Temp_F', blank=True, null=True)  # Field name made lowercase.
    daq6_enc_rh = models.FloatField(db_column='DAQ6_Enc_RH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR6Series_6_Table2'
        unique_together = (('tmstamp', 'recnum'),)


class CheverlyChevVoltFast(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    diffvolt_1 = models.FloatField(db_column='DiffVolt_1', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2 = models.FloatField(db_column='DiffVolt_2', blank=True, null=True)  # Field name made lowercase.
    probe1 = models.FloatField(blank=True, null=True)
    probe2 = models.FloatField(blank=True, null=True)
    probe3 = models.FloatField(blank=True, null=True)
    probe4 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cheverly_chev_volt_fast'
        unique_together = (('tmstamp', 'recnum'),)


class CheverlyChevVoltSlow(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    probe1_avg = models.FloatField(db_column='probe1_Avg', blank=True, null=True)  # Field name made lowercase.
    probe2_avg = models.FloatField(db_column='probe2_Avg', blank=True, null=True)  # Field name made lowercase.
    probe3_avg = models.FloatField(db_column='probe3_Avg', blank=True, null=True)  # Field name made lowercase.
    probe4_avg = models.FloatField(db_column='probe4_Avg', blank=True, null=True)  # Field name made lowercase.
    probe1_max = models.FloatField(db_column='probe1_Max', blank=True, null=True)  # Field name made lowercase.
    probe1_min = models.FloatField(db_column='probe1_Min', blank=True, null=True)  # Field name made lowercase.
    probe2_max = models.FloatField(db_column='probe2_Max', blank=True, null=True)  # Field name made lowercase.
    probe2_min = models.FloatField(db_column='probe2_Min', blank=True, null=True)  # Field name made lowercase.
    probe3_max = models.FloatField(db_column='probe3_Max', blank=True, null=True)  # Field name made lowercase.
    probe3_min = models.FloatField(db_column='probe3_Min', blank=True, null=True)  # Field name made lowercase.
    probe4_max = models.FloatField(db_column='probe4_Max', blank=True, null=True)  # Field name made lowercase.
    probe4_min = models.FloatField(db_column='probe4_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cheverly_chev_volt_slow'
        unique_together = (('tmstamp', 'recnum'),)


class CheverlyCheverlyVoltage(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    diffvolt_1 = models.FloatField(db_column='DiffVolt_1', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2 = models.FloatField(db_column='DiffVolt_2', blank=True, null=True)  # Field name made lowercase.
    probe1 = models.FloatField(blank=True, null=True)
    probe2 = models.FloatField(blank=True, null=True)
    probe1_max = models.FloatField(db_column='probe1_Max', blank=True, null=True)  # Field name made lowercase.
    probe1_min = models.FloatField(db_column='probe1_Min', blank=True, null=True)  # Field name made lowercase.
    probe2_max = models.FloatField(db_column='probe2_Max', blank=True, null=True)  # Field name made lowercase.
    probe2_min = models.FloatField(db_column='probe2_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cheverly_cheverly_voltage'
        unique_together = (('tmstamp', 'recnum'),)


class Granite9Fifteensecdata(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    staticstrain_1 = models.FloatField(db_column='StaticStrain_1', blank=True, null=True)  # Field name made lowercase.
    staticstrain_2 = models.FloatField(db_column='StaticStrain_2', blank=True, null=True)  # Field name made lowercase.
    staticstrain_3 = models.FloatField(db_column='StaticStrain_3', blank=True, null=True)  # Field name made lowercase.
    thermf_1 = models.FloatField(db_column='ThermF_1', blank=True, null=True)  # Field name made lowercase.
    thermf_2 = models.FloatField(db_column='ThermF_2', blank=True, null=True)  # Field name made lowercase.
    thermf_3 = models.FloatField(db_column='ThermF_3', blank=True, null=True)  # Field name made lowercase.
    dynstddev_1 = models.FloatField(db_column='DynStdDev_1', blank=True, null=True)  # Field name made lowercase.
    dynstddev_2 = models.FloatField(db_column='DynStdDev_2', blank=True, null=True)  # Field name made lowercase.
    dynstddev_3 = models.FloatField(db_column='DynStdDev_3', blank=True, null=True)  # Field name made lowercase.
    temp_f = models.FloatField(db_column='Temp_F', blank=True, null=True)  # Field name made lowercase.
    lvdt = models.FloatField(db_column='LVDT', blank=True, null=True)  # Field name made lowercase.
    laser0_med = models.FloatField(db_column='laser0_Med', blank=True, null=True)  # Field name made lowercase.
    lse_med = models.FloatField(db_column='LSE_Med', blank=True, null=True)  # Field name made lowercase.
    lvdt_supply = models.FloatField(db_column='LVDT_Supply', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRANITE9_FifteenSecData'
        unique_together = (('tmstamp', 'recnum'),)


class I40DsiCr6Sensors(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    sensor_data_1 = models.FloatField(db_column='Sensor_Data_1', blank=True, null=True)  # Field name made lowercase.
    sensor_data_2 = models.FloatField(db_column='Sensor_Data_2', blank=True, null=True)  # Field name made lowercase.
    sensor_data_3 = models.FloatField(db_column='Sensor_Data_3', blank=True, null=True)  # Field name made lowercase.
    sensor_data_4 = models.FloatField(db_column='Sensor_Data_4', blank=True, null=True)  # Field name made lowercase.
    sensor_data_5 = models.FloatField(db_column='Sensor_Data_5', blank=True, null=True)  # Field name made lowercase.
    sensor_data_6 = models.FloatField(db_column='Sensor_Data_6', blank=True, null=True)  # Field name made lowercase.
    sensor_data_7 = models.FloatField(db_column='Sensor_Data_7', blank=True, null=True)  # Field name made lowercase.
    sensor_data_8 = models.FloatField(db_column='Sensor_Data_8', blank=True, null=True)  # Field name made lowercase.
    sensor_data_9 = models.FloatField(db_column='Sensor_Data_9', blank=True, null=True)  # Field name made lowercase.
    sensor_data_10 = models.FloatField(db_column='Sensor_Data_10', blank=True, null=True)  # Field name made lowercase.
    sensor_data_11 = models.FloatField(db_column='Sensor_Data_11', blank=True, null=True)  # Field name made lowercase.
    sensor_data_12 = models.FloatField(db_column='Sensor_Data_12', blank=True, null=True)  # Field name made lowercase.
    sensor_data_13 = models.FloatField(db_column='Sensor_Data_13', blank=True, null=True)  # Field name made lowercase.
    sensor_data_14 = models.FloatField(db_column='Sensor_Data_14', blank=True, null=True)  # Field name made lowercase.
    sensor_data_15 = models.FloatField(db_column='Sensor_Data_15', blank=True, null=True)  # Field name made lowercase.
    sensor_data_16 = models.FloatField(db_column='Sensor_Data_16', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'I40_DSI_CR6_Sensors'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd500MainDtldata(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battvoltage = models.FloatField(db_column='battVoltage', blank=True, null=True)  # Field name made lowercase.
    ptemp = models.FloatField(db_column='pTemp', blank=True, null=True)  # Field name made lowercase.
    dtl_1_a = models.FloatField(db_column='DTL-1_A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_1_b = models.FloatField(db_column='DTL-1_B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_2_a = models.FloatField(db_column='DTL-2_A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_2_b = models.FloatField(db_column='DTL-2_B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'LADOTD_500_Main_DTLData'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd500MainTable1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_c_max = models.FloatField(db_column='PTemp_C_Max', blank=True, null=True)  # Field name made lowercase.
    amp_meter_1_max = models.FloatField(db_column='Amp_meter_1_Max', blank=True, null=True)  # Field name made lowercase.
    amp_meter_2_max = models.FloatField(db_column='Amp_meter_2_Max', blank=True, null=True)  # Field name made lowercase.
    amp_meter_3_max = models.FloatField(db_column='Amp_meter_3_Max', blank=True, null=True)  # Field name made lowercase.
    amp_meter_4_max = models.FloatField(db_column='Amp_meter_4_Max', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_500_Main_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd500MainTable2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_min = models.FloatField(db_column='BattV_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_500_Main_Table2'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd500MainEventmonitor500(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    amp_meter_1_max = models.FloatField(db_column='Amp_meter_1_Max', blank=True, null=True)  # Field name made lowercase.
    amp_meter_2_max = models.FloatField(db_column='Amp_meter_2_Max', blank=True, null=True)  # Field name made lowercase.
    amp_meter_3_max = models.FloatField(db_column='Amp_meter_3_Max', blank=True, null=True)  # Field name made lowercase.
    amp_meter_4_max = models.FloatField(db_column='Amp_meter_4_Max', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_500_Main_eventMonitor_500'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd502ETable1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_avg = models.FloatField(db_column='PTemp_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_f_ambient_avg = models.FloatField(db_column='Temp_F_Ambient_Avg', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_med = models.FloatField(db_column='Tilt_EW_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    laser3_med = models.FloatField(db_column='laser3_Med', blank=True, null=True)  # Field name made lowercase.
    laser4_med = models.FloatField(db_column='laser4_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_max = models.FloatField(db_column='Tilt_EW_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_min = models.FloatField(db_column='Tilt_EW_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_med = models.FloatField(db_column='Tilt_NS_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_max = models.FloatField(db_column='Tilt_NS_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_min = models.FloatField(db_column='Tilt_NS_Min', blank=True, null=True)  # Field name made lowercase.
    linear_pot_avg = models.FloatField(db_column='Linear_Pot_Avg', blank=True, null=True)  # Field name made lowercase.
    linear_pot_max = models.FloatField(db_column='Linear_Pot_Max', blank=True, null=True)  # Field name made lowercase.
    linear_pot_min = models.FloatField(db_column='Linear_Pot_Min', blank=True, null=True)  # Field name made lowercase.
    linear_pot2_avg = models.FloatField(db_column='Linear_Pot2_Avg', blank=True, null=True)  # Field name made lowercase.
    linear_pot2_max = models.FloatField(db_column='Linear_Pot2_Max', blank=True, null=True)  # Field name made lowercase.
    linear_pot2_min = models.FloatField(db_column='Linear_Pot2_Min', blank=True, null=True)  # Field name made lowercase.
    laserjt_avg = models.FloatField(db_column='LaserJt_Avg', blank=True, null=True)  # Field name made lowercase.
    laserjt_max = models.FloatField(db_column='LaserJt_Max', blank=True, null=True)  # Field name made lowercase.
    laserjt_min = models.FloatField(db_column='LaserJt_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_502_E_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd502ETable1Arch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_avg = models.FloatField(db_column='PTemp_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_f_ambient_avg = models.FloatField(db_column='Temp_F_Ambient_Avg', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_med = models.FloatField(db_column='Tilt_EW_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    laser3_med = models.FloatField(db_column='laser3_Med', blank=True, null=True)  # Field name made lowercase.
    laser4_med = models.FloatField(db_column='laser4_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_max = models.FloatField(db_column='Tilt_EW_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_min = models.FloatField(db_column='Tilt_EW_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_502_E_Table1_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd502EEventmonitor502(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    tilt_ew = models.FloatField(db_column='Tilt_EW', blank=True, null=True)  # Field name made lowercase.
    laser1 = models.FloatField(blank=True, null=True)
    laser2 = models.FloatField(blank=True, null=True)
    laser3 = models.FloatField(blank=True, null=True)
    laser4 = models.FloatField(blank=True, null=True)
    linear_pot = models.FloatField(db_column='Linear_Pot', blank=True, null=True)  # Field name made lowercase.
    linear_pot2 = models.FloatField(db_column='Linear_Pot2', blank=True, null=True)  # Field name made lowercase.
    tilt_ns = models.FloatField(db_column='Tilt_NS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_502_E_eventMonitor_502'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd502EEventmonitor502Arch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    tilt_ew = models.FloatField(db_column='Tilt_EW', blank=True, null=True)  # Field name made lowercase.
    laser1 = models.FloatField(blank=True, null=True)
    laser2 = models.FloatField(blank=True, null=True)
    laser3 = models.FloatField(blank=True, null=True)
    laser4 = models.FloatField(blank=True, null=True)
    linear_pot = models.FloatField(db_column='Linear_Pot', blank=True, null=True)  # Field name made lowercase.
    linear_pot2 = models.FloatField(db_column='Linear_Pot2', blank=True, null=True)  # Field name made lowercase.
    tilt_ns = models.FloatField(db_column='Tilt_NS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_502_E_eventMonitor_502_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd502EEvent502(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    lne = models.FloatField(db_column='LNE', blank=True, null=True)  # Field name made lowercase.
    tne = models.FloatField(db_column='TNE', blank=True, null=True)  # Field name made lowercase.
    vne = models.FloatField(db_column='VNE', blank=True, null=True)  # Field name made lowercase.
    se_shoe = models.FloatField(db_column='SE_Shoe', blank=True, null=True)  # Field name made lowercase.
    ne_shoe = models.FloatField(db_column='NE_Shoe', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns = models.FloatField(db_column='Tilt_about_NS', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew = models.FloatField(db_column='Tilt_about_EW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_502_E_event_502'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd502EMonitor502(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_avg = models.FloatField(db_column='PTemp_Avg', blank=True, null=True)  # Field name made lowercase.
    laser0_med = models.FloatField(db_column='laser0_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    lne_med = models.FloatField(db_column='LNE_Med', blank=True, null=True)  # Field name made lowercase.
    tne_med = models.FloatField(db_column='TNE_Med', blank=True, null=True)  # Field name made lowercase.
    vne_med = models.FloatField(db_column='VNE_Med', blank=True, null=True)  # Field name made lowercase.
    se_shoe_avg = models.FloatField(db_column='SE_Shoe_Avg', blank=True, null=True)  # Field name made lowercase.
    se_shoe_max = models.FloatField(db_column='SE_Shoe_Max', blank=True, null=True)  # Field name made lowercase.
    se_shoe_min = models.FloatField(db_column='SE_Shoe_Min', blank=True, null=True)  # Field name made lowercase.
    ne_shoe_avg = models.FloatField(db_column='NE_Shoe_Avg', blank=True, null=True)  # Field name made lowercase.
    ne_shoe_max = models.FloatField(db_column='NE_Shoe_Max', blank=True, null=True)  # Field name made lowercase.
    ne_shoe_min = models.FloatField(db_column='NE_Shoe_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_med = models.FloatField(db_column='Tilt_about_NS_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_max = models.FloatField(db_column='Tilt_about_NS_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_min = models.FloatField(db_column='Tilt_about_NS_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_med = models.FloatField(db_column='Tilt_about_EW_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_max = models.FloatField(db_column='Tilt_about_EW_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_min = models.FloatField(db_column='Tilt_about_EW_Min', blank=True, null=True)  # Field name made lowercase.
    e_joint_laser_avg = models.FloatField(db_column='E_joint_laser_Avg', blank=True, null=True)  # Field name made lowercase.
    e_joint_laser_max = models.FloatField(db_column='E_joint_laser_Max', blank=True, null=True)  # Field name made lowercase.
    e_joint_laser_min = models.FloatField(db_column='E_joint_laser_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_502_E_monitor_502'
        unique_together = (('tmstamp', 'recnum'),)


class Ladotd502EZero502(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    ne_shoe_zero = models.FloatField(db_column='NE_Shoe_zero', blank=True, null=True)  # Field name made lowercase.
    se_shoe_zero = models.FloatField(db_column='SE_Shoe_zero', blank=True, null=True)  # Field name made lowercase.
    lne_zero = models.FloatField(db_column='LNE_zero', blank=True, null=True)  # Field name made lowercase.
    tne_zero = models.FloatField(db_column='TNE_zero', blank=True, null=True)  # Field name made lowercase.
    vne_zero = models.FloatField(db_column='VNE_zero', blank=True, null=True)  # Field name made lowercase.
    e_joint_laser = models.FloatField(db_column='E_joint_laser', blank=True, null=True)  # Field name made lowercase.
    e_joint_laser_zero = models.FloatField(db_column='E_joint_laser_zero', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_zero = models.FloatField(db_column='Tilt_about_EW_zero', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_zero = models.FloatField(db_column='Tilt_about_NS_zero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOTD_502_E_zero_502'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot501WTable1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_avg = models.FloatField(db_column='PTemp_Avg', blank=True, null=True)  # Field name made lowercase.
    linear_pot_avg = models.FloatField(db_column='Linear_Pot_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_c_top_avg = models.FloatField(db_column='Temp_C_Top_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_c_bottom_avg = models.FloatField(db_column='Temp_C_Bottom_Avg', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_med = models.FloatField(db_column='Tilt_NS_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    laser3_med = models.FloatField(db_column='laser3_Med', blank=True, null=True)  # Field name made lowercase.
    laser4_med = models.FloatField(db_column='laser4_Med', blank=True, null=True)  # Field name made lowercase.
    linear_pot_max = models.FloatField(db_column='Linear_Pot_Max', blank=True, null=True)  # Field name made lowercase.
    linear_pot_min = models.FloatField(db_column='Linear_Pot_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_max = models.FloatField(db_column='Tilt_NS_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_min = models.FloatField(db_column='Tilt_NS_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_med = models.FloatField(db_column='Tilt_EW_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_max = models.FloatField(db_column='Tilt_EW_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_ew_min = models.FloatField(db_column='Tilt_EW_Min', blank=True, null=True)  # Field name made lowercase.
    linear_pot2_avg = models.FloatField(db_column='Linear_Pot2_Avg', blank=True, null=True)  # Field name made lowercase.
    linear_pot2_max = models.FloatField(db_column='Linear_Pot2_Max', blank=True, null=True)  # Field name made lowercase.
    linear_pot2_min = models.FloatField(db_column='Linear_Pot2_Min', blank=True, null=True)  # Field name made lowercase.
    laserjt_avg = models.FloatField(db_column='LaserJt_Avg', blank=True, null=True)  # Field name made lowercase.
    laserjt_max = models.FloatField(db_column='LaserJt_Max', blank=True, null=True)  # Field name made lowercase.
    laserjt_min = models.FloatField(db_column='LaserJt_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_501_W_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot501WTable1Arch(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.
    linear_pot_max = models.FloatField(db_column='Linear_Pot_Max', blank=True, null=True)  # Field name made lowercase.
    temp_c_top_max = models.FloatField(db_column='Temp_C_Top_Max', blank=True, null=True)  # Field name made lowercase.
    temp_c_bottom_max = models.FloatField(db_column='Temp_C_Bottom_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_sn_max = models.FloatField(db_column='Tilt_SN_Max', blank=True, null=True)  # Field name made lowercase.
    laser1 = models.FloatField(blank=True, null=True)
    laser2 = models.FloatField(blank=True, null=True)
    laser3 = models.FloatField(blank=True, null=True)
    laser4 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LADOT_501_W_Table1_arch'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot501WTable1Arch2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_avg = models.FloatField(db_column='PTemp_Avg', blank=True, null=True)  # Field name made lowercase.
    linear_pot_avg = models.FloatField(db_column='Linear_Pot_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_c_top_avg = models.FloatField(db_column='Temp_C_Top_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_c_bottom_avg = models.FloatField(db_column='Temp_C_Bottom_Avg', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_med = models.FloatField(db_column='Tilt_NS_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    laser3_med = models.FloatField(db_column='laser3_Med', blank=True, null=True)  # Field name made lowercase.
    laser4_med = models.FloatField(db_column='laser4_Med', blank=True, null=True)  # Field name made lowercase.
    linear_pot_max = models.FloatField(db_column='Linear_Pot_Max', blank=True, null=True)  # Field name made lowercase.
    linear_pot_min = models.FloatField(db_column='Linear_Pot_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_max = models.FloatField(db_column='Tilt_NS_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_ns_min = models.FloatField(db_column='Tilt_NS_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_501_W_Table1_arch2'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot501WEventmonitor501(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    linear_pot = models.FloatField(db_column='Linear_Pot', blank=True, null=True)  # Field name made lowercase.
    tilt_ns = models.FloatField(db_column='Tilt_NS', blank=True, null=True)  # Field name made lowercase.
    laser1 = models.FloatField(blank=True, null=True)
    laser2 = models.FloatField(blank=True, null=True)
    laser3 = models.FloatField(blank=True, null=True)
    laser4 = models.FloatField(blank=True, null=True)
    linear_pot2 = models.FloatField(db_column='Linear_Pot2', blank=True, null=True)  # Field name made lowercase.
    tilt_ew = models.FloatField(db_column='Tilt_EW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_501_W_eventMonitor_501'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot501WEvent501(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    lnw = models.FloatField(db_column='LNW', blank=True, null=True)  # Field name made lowercase.
    tnw = models.FloatField(db_column='TNW', blank=True, null=True)  # Field name made lowercase.
    vnw = models.FloatField(db_column='VNW', blank=True, null=True)  # Field name made lowercase.
    sw_shoe = models.FloatField(db_column='SW_Shoe', blank=True, null=True)  # Field name made lowercase.
    nw_shoe = models.FloatField(db_column='NW_Shoe', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns = models.FloatField(db_column='Tilt_about_NS', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew = models.FloatField(db_column='Tilt_about_EW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_501_W_event_501'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot501WMonitor501(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_avg = models.FloatField(db_column='BattV_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp_avg = models.FloatField(db_column='PTemp_Avg', blank=True, null=True)  # Field name made lowercase.
    laser0_med = models.FloatField(db_column='laser0_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    lnw_med = models.FloatField(db_column='LNW_Med', blank=True, null=True)  # Field name made lowercase.
    tnw_med = models.FloatField(db_column='TNW_Med', blank=True, null=True)  # Field name made lowercase.
    vnw_med = models.FloatField(db_column='VNW_Med', blank=True, null=True)  # Field name made lowercase.
    sw_shoe_avg = models.FloatField(db_column='SW_Shoe_Avg', blank=True, null=True)  # Field name made lowercase.
    sw_shoe_max = models.FloatField(db_column='SW_Shoe_Max', blank=True, null=True)  # Field name made lowercase.
    sw_shoe_min = models.FloatField(db_column='SW_Shoe_Min', blank=True, null=True)  # Field name made lowercase.
    nw_shoe_avg = models.FloatField(db_column='NW_Shoe_Avg', blank=True, null=True)  # Field name made lowercase.
    nw_shoe_max = models.FloatField(db_column='NW_Shoe_Max', blank=True, null=True)  # Field name made lowercase.
    nw_shoe_min = models.FloatField(db_column='NW_Shoe_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_med = models.FloatField(db_column='Tilt_about_NS_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_max = models.FloatField(db_column='Tilt_about_NS_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_min = models.FloatField(db_column='Tilt_about_NS_Min', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_med = models.FloatField(db_column='Tilt_about_EW_Med', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_max = models.FloatField(db_column='Tilt_about_EW_Max', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_min = models.FloatField(db_column='Tilt_about_EW_Min', blank=True, null=True)  # Field name made lowercase.
    w_joint_laser_avg = models.FloatField(db_column='W_joint_laser_Avg', blank=True, null=True)  # Field name made lowercase.
    w_joint_laser_max = models.FloatField(db_column='W_joint_laser_Max', blank=True, null=True)  # Field name made lowercase.
    w_joint_laser_min = models.FloatField(db_column='W_joint_laser_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_501_W_monitor_501'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot501WZero501(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    nw_shoe_zero = models.FloatField(db_column='NW_Shoe_zero', blank=True, null=True)  # Field name made lowercase.
    sw_shoe_zero = models.FloatField(db_column='SW_Shoe_zero', blank=True, null=True)  # Field name made lowercase.
    lnw_zero = models.FloatField(db_column='LNW_zero', blank=True, null=True)  # Field name made lowercase.
    tnw_zero = models.FloatField(db_column='TNW_zero', blank=True, null=True)  # Field name made lowercase.
    vnw_zero = models.FloatField(db_column='VNW_zero', blank=True, null=True)  # Field name made lowercase.
    w_joint_laser = models.FloatField(db_column='W_joint_laser', blank=True, null=True)  # Field name made lowercase.
    w_joint_laser_zero = models.FloatField(db_column='W_joint_laser_zero', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ns_zero = models.FloatField(db_column='Tilt_about_NS_zero', blank=True, null=True)  # Field name made lowercase.
    tilt_about_ew_zero = models.FloatField(db_column='Tilt_about_EW_zero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_501_W_zero_501'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot601WDtldata(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battvoltage = models.FloatField(db_column='battVoltage', blank=True, null=True)  # Field name made lowercase.
    ptemp = models.FloatField(db_column='PTemp', blank=True, null=True)  # Field name made lowercase.
    dtl_1_a = models.FloatField(db_column='DTL-1_A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_1_b = models.FloatField(db_column='DTL-1_B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_2_a = models.FloatField(db_column='DTL-2_A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_2_b = models.FloatField(db_column='DTL-2_B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'LADOT_601_W_DTLData'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot601WTable1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    temp_c_top_avg = models.FloatField(db_column='Temp_C_Top_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_c_bottom_avg = models.FloatField(db_column='Temp_C_Bottom_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_601_W_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot601WEventmonitor601(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    laser1 = models.FloatField(blank=True, null=True)
    laser2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LADOT_601_W_eventMonitor_601'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot601WEvent601(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    lsw = models.FloatField(db_column='LSW', blank=True, null=True)  # Field name made lowercase.
    tsw = models.FloatField(db_column='TSW', blank=True, null=True)  # Field name made lowercase.
    vsw = models.FloatField(db_column='VSW', blank=True, null=True)  # Field name made lowercase.
    lnw_ultra_in = models.FloatField(db_column='LNW_ultra_in', blank=True, null=True)  # Field name made lowercase.
    lsw_ultra_in = models.FloatField(db_column='LSW_ultra_in', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_601_W_event_601'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot601WMonitor601(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.
    laser0_med = models.FloatField(db_column='laser0_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    lsw_med = models.FloatField(db_column='LSW_Med', blank=True, null=True)  # Field name made lowercase.
    tsw_med = models.FloatField(db_column='TSW_Med', blank=True, null=True)  # Field name made lowercase.
    vsw_med = models.FloatField(db_column='VSW_Med', blank=True, null=True)  # Field name made lowercase.
    temp_top_avg = models.FloatField(db_column='Temp_Top_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_bottom_avg = models.FloatField(db_column='Temp_Bottom_Avg', blank=True, null=True)  # Field name made lowercase.
    lnw_ultra_in_med = models.FloatField(db_column='LNW_ultra_in_Med', blank=True, null=True)  # Field name made lowercase.
    lsw_ultra_in_med = models.FloatField(db_column='LSW_ultra_in_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_601_W_monitor_601'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot601WZero601(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    lsw_zero = models.FloatField(db_column='LSW_zero', blank=True, null=True)  # Field name made lowercase.
    tsw_zero = models.FloatField(db_column='TSW_zero', blank=True, null=True)  # Field name made lowercase.
    vsw_zero = models.FloatField(db_column='VSW_zero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_601_W_zero_601'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot602ETable1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    temp_f_ambient_avg = models.FloatField(db_column='Temp_F_Ambient_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_602_E_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot602EEventmonitor602(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    laser1 = models.FloatField(blank=True, null=True)
    laser2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LADOT_602_E_eventMonitor_602'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot602EEvent602(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    lse = models.FloatField(db_column='LSE', blank=True, null=True)  # Field name made lowercase.
    tse = models.FloatField(db_column='TSE', blank=True, null=True)  # Field name made lowercase.
    vse = models.FloatField(db_column='VSE', blank=True, null=True)  # Field name made lowercase.
    lne_ultra_in = models.FloatField(db_column='LNE_ultra_in', blank=True, null=True)  # Field name made lowercase.
    tne_ultra_in = models.FloatField(db_column='TNE_ultra_in', blank=True, null=True)  # Field name made lowercase.
    lse_ultra_in = models.FloatField(db_column='LSE_ultra_in', blank=True, null=True)  # Field name made lowercase.
    tse_ultra_in = models.FloatField(db_column='TSE_ultra_in', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_602_E_event_602'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot602EMonitor602(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.
    laser0_med = models.FloatField(db_column='laser0_Med', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    lse_med = models.FloatField(db_column='LSE_Med', blank=True, null=True)  # Field name made lowercase.
    tse_med = models.FloatField(db_column='TSE_Med', blank=True, null=True)  # Field name made lowercase.
    vse_med = models.FloatField(db_column='VSE_Med', blank=True, null=True)  # Field name made lowercase.
    temp_ambient_avg = models.FloatField(db_column='Temp_Ambient_Avg', blank=True, null=True)  # Field name made lowercase.
    lne_ultra_in_med = models.FloatField(db_column='LNE_ultra_in_Med', blank=True, null=True)  # Field name made lowercase.
    tne_ultra_in_med = models.FloatField(db_column='TNE_ultra_in_Med', blank=True, null=True)  # Field name made lowercase.
    lse_ultra_in_med = models.FloatField(db_column='LSE_ultra_in_Med', blank=True, null=True)  # Field name made lowercase.
    tse_ultra_in_med = models.FloatField(db_column='TSE_ultra_in_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_602_E_monitor_602'
        unique_together = (('tmstamp', 'recnum'),)


class Ladot602EZero602(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    lse_zero = models.FloatField(db_column='LSE_zero', blank=True, null=True)  # Field name made lowercase.
    tse_zero = models.FloatField(db_column='TSE_zero', blank=True, null=True)  # Field name made lowercase.
    vse_zero = models.FloatField(db_column='VSE_zero', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_602_E_zero_602'
        unique_together = (('tmstamp', 'recnum'),)


class Lndbcolumnmeta(models.Model):
    columnid = models.AutoField(db_column='columnID', primary_key=True)  # Field name made lowercase.
    lndbstationmeta_stationid = models.ForeignKey('Lndbstationmeta', models.DO_NOTHING, db_column='LNDBStationMeta_stationID')  # Field name made lowercase.
    lndbtablemeta_tableid = models.ForeignKey('Lndbtablemeta', models.DO_NOTHING, db_column='LNDBTableMeta_tableID')  # Field name made lowercase.
    lncolumnname = models.TextField(db_column='lnColumnName', blank=True, null=True)  # Field name made lowercase.
    dbcolumnname = models.TextField(db_column='dbColumnName', blank=True, null=True)  # Field name made lowercase.
    process = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    datatype = models.IntegerField(db_column='dataType', blank=True, null=True)  # Field name made lowercase.
    columnorder = models.BigIntegerField(db_column='columnOrder', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LNDBColumnMeta'


class Lndbstationmeta(models.Model):
    stationid = models.AutoField(db_column='stationID', primary_key=True)  # Field name made lowercase.
    lnstationname = models.TextField(db_column='lnStationName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LNDBStationMeta'


class Lndbtablemeta(models.Model):
    tableid = models.AutoField(db_column='tableID', primary_key=True)  # Field name made lowercase.
    lndbstationmeta_stationid = models.ForeignKey(Lndbstationmeta, models.DO_NOTHING, db_column='LNDBStationMeta_stationID')  # Field name made lowercase.
    lntablename = models.TextField(db_column='lnTableName', blank=True, null=True)  # Field name made lowercase.
    dbtablename = models.TextField(db_column='dbTableName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LNDBTableMeta'


class Lulling1Table1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv = models.FloatField(db_column='BattV', blank=True, null=True)  # Field name made lowercase.
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.
    sys1_loc1_strain_s = models.FloatField(db_column='Sys1_Loc1_Strain_S', blank=True, null=True)  # Field name made lowercase.
    vr1000_s_1 = models.FloatField(db_column='Vr1000_S_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_s_2 = models.FloatField(db_column='Vr1000_S_2', blank=True, null=True)  # Field name made lowercase.
    sys1_loc2_strain_s = models.FloatField(db_column='Sys1_Loc2_Strain_S', blank=True, null=True)  # Field name made lowercase.
    sys1_loc1_strain_e = models.FloatField(db_column='Sys1_Loc1_Strain_E', blank=True, null=True)  # Field name made lowercase.
    vr1000_e_1 = models.FloatField(db_column='Vr1000_E_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_e_2 = models.FloatField(db_column='Vr1000_E_2', blank=True, null=True)  # Field name made lowercase.
    sys1_loc2_strain_e = models.FloatField(db_column='Sys1_Loc2_Strain_E', blank=True, null=True)  # Field name made lowercase.
    sys1_loc1_strain_c1 = models.FloatField(db_column='Sys1_Loc1_Strain_C1', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_1 = models.FloatField(db_column='Vr1000_C_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_2 = models.FloatField(db_column='Vr1000_C_2', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_3 = models.FloatField(db_column='Vr1000_C_3', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_4 = models.FloatField(db_column='Vr1000_C_4', blank=True, null=True)  # Field name made lowercase.
    sys1_loc1_strain_c2 = models.FloatField(db_column='Sys1_Loc1_Strain_C2', blank=True, null=True)  # Field name made lowercase.
    sys1_loc2_strain_c1 = models.FloatField(db_column='Sys1_Loc2_Strain_C1', blank=True, null=True)  # Field name made lowercase.
    sys1_loc2_strain_c2 = models.FloatField(db_column='Sys1_Loc2_Strain_C2', blank=True, null=True)  # Field name made lowercase.
    sys1_temp_c_s = models.FloatField(db_column='Sys1_Temp_C_S', blank=True, null=True)  # Field name made lowercase.
    sys1_temp_c_e = models.FloatField(db_column='Sys1_Temp_C_E', blank=True, null=True)  # Field name made lowercase.
    sys1_temp_c_c1 = models.FloatField(db_column='Sys1_Temp_C_C1', blank=True, null=True)  # Field name made lowercase.
    sys1_temp_c_c2 = models.FloatField(db_column='Sys1_Temp_C_C2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lulling_1_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Lulling2Table1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv = models.FloatField(db_column='BattV', blank=True, null=True)  # Field name made lowercase.
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.
    sys2_loc1_strain_s = models.FloatField(db_column='Sys2_Loc1_Strain_S', blank=True, null=True)  # Field name made lowercase.
    vr1000_s_1 = models.FloatField(db_column='Vr1000_S_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_s_2 = models.FloatField(db_column='Vr1000_S_2', blank=True, null=True)  # Field name made lowercase.
    sys2_loc2_strain_s = models.FloatField(db_column='Sys2_Loc2_Strain_S', blank=True, null=True)  # Field name made lowercase.
    sys2_loc1_strain_e = models.FloatField(db_column='Sys2_Loc1_Strain_E', blank=True, null=True)  # Field name made lowercase.
    vr1000_e_1 = models.FloatField(db_column='Vr1000_E_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_e_2 = models.FloatField(db_column='Vr1000_E_2', blank=True, null=True)  # Field name made lowercase.
    sys2_loc2_strain_e = models.FloatField(db_column='Sys2_Loc2_Strain_E', blank=True, null=True)  # Field name made lowercase.
    sys2_loc1_strain_c1 = models.FloatField(db_column='Sys2_Loc1_Strain_C1', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_1 = models.FloatField(db_column='Vr1000_C_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_2 = models.FloatField(db_column='Vr1000_C_2', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_3 = models.FloatField(db_column='Vr1000_C_3', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_4 = models.FloatField(db_column='Vr1000_C_4', blank=True, null=True)  # Field name made lowercase.
    sys2_loc1_strain_c2 = models.FloatField(db_column='Sys2_Loc1_Strain_C2', blank=True, null=True)  # Field name made lowercase.
    sys2_loc2_strain_c1 = models.FloatField(db_column='Sys2_Loc2_Strain_C1', blank=True, null=True)  # Field name made lowercase.
    sys2_loc2_strain_c2 = models.FloatField(db_column='Sys2_Loc2_Strain_C2', blank=True, null=True)  # Field name made lowercase.
    sys2_temp_c_s = models.FloatField(db_column='Sys2_Temp_C_S', blank=True, null=True)  # Field name made lowercase.
    sys2_temp_c_e = models.FloatField(db_column='Sys2_Temp_C_E', blank=True, null=True)  # Field name made lowercase.
    sys2_temp_c_c1 = models.FloatField(db_column='Sys2_Temp_C_C1', blank=True, null=True)  # Field name made lowercase.
    sys2_temp_c_c2 = models.FloatField(db_column='Sys2_Temp_C_C2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lulling_2_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Lulling3Table1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv = models.FloatField(db_column='BattV', blank=True, null=True)  # Field name made lowercase.
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.
    sys3_loc1_strain_s = models.FloatField(db_column='Sys3_Loc1_Strain_S', blank=True, null=True)  # Field name made lowercase.
    vr1000_s_1 = models.FloatField(db_column='Vr1000_S_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_s_2 = models.FloatField(db_column='Vr1000_S_2', blank=True, null=True)  # Field name made lowercase.
    sys3_loc2_strain_s = models.FloatField(db_column='Sys3_Loc2_Strain_S', blank=True, null=True)  # Field name made lowercase.
    sys3_loc1_strain_e = models.FloatField(db_column='Sys3_Loc1_Strain_E', blank=True, null=True)  # Field name made lowercase.
    vr1000_e_1 = models.FloatField(db_column='Vr1000_E_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_e_2 = models.FloatField(db_column='Vr1000_E_2', blank=True, null=True)  # Field name made lowercase.
    sys3_loc2_strain_e = models.FloatField(db_column='Sys3_Loc2_Strain_E', blank=True, null=True)  # Field name made lowercase.
    sys3_loc1_strain_c1 = models.FloatField(db_column='Sys3_Loc1_Strain_C1', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_1 = models.FloatField(db_column='Vr1000_C_1', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_2 = models.FloatField(db_column='Vr1000_C_2', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_3 = models.FloatField(db_column='Vr1000_C_3', blank=True, null=True)  # Field name made lowercase.
    vr1000_c_4 = models.FloatField(db_column='Vr1000_C_4', blank=True, null=True)  # Field name made lowercase.
    sys3_loc1_strain_c2 = models.FloatField(db_column='Sys3_Loc1_Strain_C2', blank=True, null=True)  # Field name made lowercase.
    sys3_loc2_strain_c1 = models.FloatField(db_column='Sys3_Loc2_Strain_C1', blank=True, null=True)  # Field name made lowercase.
    sys3_loc2_strain_c2 = models.FloatField(db_column='Sys3_Loc2_Strain_C2', blank=True, null=True)  # Field name made lowercase.
    sys3_temp_c_s = models.FloatField(db_column='Sys3_Temp_C_S', blank=True, null=True)  # Field name made lowercase.
    sys3_temp_c_e = models.FloatField(db_column='Sys3_Temp_C_E', blank=True, null=True)  # Field name made lowercase.
    sys3_temp_c_c1 = models.FloatField(db_column='Sys3_Temp_C_C1', blank=True, null=True)  # Field name made lowercase.
    sys3_temp_c_c2 = models.FloatField(db_column='Sys3_Temp_C_C2', blank=True, null=True)  # Field name made lowercase.
    vr1000_s_3 = models.FloatField(db_column='Vr1000_S_3', blank=True, null=True)  # Field name made lowercase.
    sys3_loc3_strain_s = models.FloatField(db_column='Sys3_Loc3_Strain_S', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lulling_3_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class McleanMcleanmeasure(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    temptilt_a = models.FloatField(blank=True, null=True)
    temptilt_b = models.FloatField(blank=True, null=True)
    tilt_a_deg = models.FloatField(blank=True, null=True)
    tilt_b_deg = models.FloatField(blank=True, null=True)
    laser1 = models.FloatField(blank=True, null=True)
    stringdisp = models.FloatField(db_column='stringDisp', blank=True, null=True)  # Field name made lowercase.
    sevolt = models.FloatField(db_column='SEVolt', blank=True, null=True)  # Field name made lowercase.
    tilt_temp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mclean_McleanMeasure'
        unique_together = (('tmstamp', 'recnum'),)


class McleanTable1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mclean_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Ny17Mediandata(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    laser_18_med = models.FloatField(db_column='laser_18_Med', blank=True, null=True)  # Field name made lowercase.
    laser_19_med = models.FloatField(db_column='laser_19_Med', blank=True, null=True)  # Field name made lowercase.
    laser_29_med = models.FloatField(db_column='laser_29_Med', blank=True, null=True)  # Field name made lowercase.
    laser_40_med = models.FloatField(db_column='laser_40_Med', blank=True, null=True)  # Field name made lowercase.
    temp_18_med = models.FloatField(db_column='temp_18_Med', blank=True, null=True)  # Field name made lowercase.
    temp_19_med = models.FloatField(db_column='temp_19_Med', blank=True, null=True)  # Field name made lowercase.
    temp_29_med = models.FloatField(db_column='temp_29_Med', blank=True, null=True)  # Field name made lowercase.
    temp_40_med = models.FloatField(db_column='temp_40_Med', blank=True, null=True)  # Field name made lowercase.
    laser_18in_med = models.FloatField(db_column='laser_18in_Med', blank=True, null=True)  # Field name made lowercase.
    laser_19in_med = models.FloatField(db_column='laser_19in_Med', blank=True, null=True)  # Field name made lowercase.
    laser_29in_med = models.FloatField(db_column='laser_29in_Med', blank=True, null=True)  # Field name made lowercase.
    laser_40in_med = models.FloatField(db_column='laser_40in_Med', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NY17_MedianData'
        unique_together = (('tmstamp', 'recnum'),)


class Ny17Table1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    laser_18_avg = models.FloatField(db_column='laser_18_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_19_avg = models.FloatField(db_column='laser_19_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_29_avg = models.FloatField(db_column='laser_29_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_40_avg = models.FloatField(db_column='laser_40_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_18in_avg = models.FloatField(db_column='laser_18in_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_19in_avg = models.FloatField(db_column='laser_19in_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_29in_avg = models.FloatField(db_column='laser_29in_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_40in_avg = models.FloatField(db_column='laser_40in_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_18_avg = models.FloatField(db_column='temp_18_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_19_avg = models.FloatField(db_column='temp_19_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_29_avg = models.FloatField(db_column='temp_29_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_40_avg = models.FloatField(db_column='temp_40_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NY17_Table1'
        unique_together = (('tmstamp', 'recnum'),)


class Ny17Table1Arch1(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    diffvolt_avg_1 = models.FloatField(db_column='DiffVolt_Avg_1', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_2 = models.FloatField(db_column='DiffVolt_Avg_2', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_3 = models.FloatField(db_column='DiffVolt_Avg_3', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_4 = models.FloatField(db_column='DiffVolt_Avg_4', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_5 = models.FloatField(db_column='DiffVolt_Avg_5', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_6 = models.FloatField(db_column='DiffVolt_Avg_6', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_7 = models.FloatField(db_column='DiffVolt_Avg_7', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_8 = models.FloatField(db_column='DiffVolt_Avg_8', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_9 = models.FloatField(db_column='DiffVolt_Avg_9', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_10 = models.FloatField(db_column='DiffVolt_Avg_10', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_11 = models.FloatField(db_column='DiffVolt_Avg_11', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_12 = models.FloatField(db_column='DiffVolt_Avg_12', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_13 = models.FloatField(db_column='DiffVolt_Avg_13', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_14 = models.FloatField(db_column='DiffVolt_Avg_14', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_15 = models.FloatField(db_column='DiffVolt_Avg_15', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_16 = models.FloatField(db_column='DiffVolt_Avg_16', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_1 = models.FloatField(db_column='DiffVolt_2_Avg_1', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_2 = models.FloatField(db_column='DiffVolt_2_Avg_2', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_3 = models.FloatField(db_column='DiffVolt_2_Avg_3', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_4 = models.FloatField(db_column='DiffVolt_2_Avg_4', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_5 = models.FloatField(db_column='DiffVolt_2_Avg_5', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_6 = models.FloatField(db_column='DiffVolt_2_Avg_6', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_7 = models.FloatField(db_column='DiffVolt_2_Avg_7', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_8 = models.FloatField(db_column='DiffVolt_2_Avg_8', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_9 = models.FloatField(db_column='DiffVolt_2_Avg_9', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_10 = models.FloatField(db_column='DiffVolt_2_Avg_10', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_11 = models.FloatField(db_column='DiffVolt_2_Avg_11', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_12 = models.FloatField(db_column='DiffVolt_2_Avg_12', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_13 = models.FloatField(db_column='DiffVolt_2_Avg_13', blank=True, null=True)  # Field name made lowercase.
    laser_avg_1 = models.FloatField(db_column='laser_Avg_1', blank=True, null=True)  # Field name made lowercase.
    laser_avg_2 = models.FloatField(db_column='laser_Avg_2', blank=True, null=True)  # Field name made lowercase.
    laser_avg_3 = models.FloatField(db_column='laser_Avg_3', blank=True, null=True)  # Field name made lowercase.
    temp_f_avg_1 = models.FloatField(db_column='Temp_F_Avg_1', blank=True, null=True)  # Field name made lowercase.
    temp_f_avg_2 = models.FloatField(db_column='Temp_F_Avg_2', blank=True, null=True)  # Field name made lowercase.
    temp_f_avg_3 = models.FloatField(db_column='Temp_F_Avg_3', blank=True, null=True)  # Field name made lowercase.
    laser_18_avg = models.FloatField(db_column='laser_18_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_19_avg = models.FloatField(db_column='laser_19_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_29_avg = models.FloatField(db_column='laser_29_Avg', blank=True, null=True)  # Field name made lowercase.
    laser_40_avg = models.FloatField(db_column='laser_40_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_18_avg = models.FloatField(db_column='temp_18_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_19_avg = models.FloatField(db_column='temp_19_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_29_avg = models.FloatField(db_column='temp_29_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_40_avg = models.FloatField(db_column='temp_40_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NY17_Table1_arch1'
        unique_together = (('tmstamp', 'recnum'),)


class Ny17Table2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_min = models.FloatField(db_column='BattV_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NY17_Table2'
        unique_together = (('tmstamp', 'recnum'),)


class Ny17Table3(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    crk_18_1_avg = models.FloatField(db_column='crk_18_1_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_18_2_avg = models.FloatField(db_column='crk_18_2_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_18_3_avg = models.FloatField(db_column='crk_18_3_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_18_4_avg = models.FloatField(db_column='crk_18_4_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_18_5_avg = models.FloatField(db_column='crk_18_5_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_18_6_avg = models.FloatField(db_column='crk_18_6_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_18_7_avg = models.FloatField(db_column='crk_18_7_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_19_1_avg = models.FloatField(db_column='crk_19_1_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_19_2_avg = models.FloatField(db_column='crk_19_2_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_19_3_avg = models.FloatField(db_column='crk_19_3_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_19_4_avg = models.FloatField(db_column='crk_19_4_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_19_5_avg = models.FloatField(db_column='crk_19_5_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_28_1_avg = models.FloatField(db_column='crk_28_1_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_28_2_avg = models.FloatField(db_column='crk_28_2_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_28_3_avg = models.FloatField(db_column='crk_28_3_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_28_4_avg = models.FloatField(db_column='crk_28_4_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_28_5_avg = models.FloatField(db_column='crk_28_5_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_29_1_avg = models.FloatField(db_column='crk_29_1_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_29_2_avg = models.FloatField(db_column='crk_29_2_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_29_3_avg = models.FloatField(db_column='crk_29_3_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_29_4_avg = models.FloatField(db_column='crk_29_4_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_40_1_avg = models.FloatField(db_column='crk_40_1_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_40_2_avg = models.FloatField(db_column='crk_40_2_Avg', blank=True, null=True)  # Field name made lowercase.
    crk_40_3_avg = models.FloatField(db_column='crk_40_3_Avg', blank=True, null=True)  # Field name made lowercase.
    dummy_avg = models.FloatField(db_column='dummy_Avg', blank=True, null=True)  # Field name made lowercase.
    lsr_18_avg = models.FloatField(db_column='lsr_18_Avg', blank=True, null=True)  # Field name made lowercase.
    lsr_19_avg = models.FloatField(db_column='lsr_19_Avg', blank=True, null=True)  # Field name made lowercase.
    lsr_29_avg = models.FloatField(db_column='lsr_29_Avg', blank=True, null=True)  # Field name made lowercase.
    lsr_40_avg = models.FloatField(db_column='lsr_40_Avg', blank=True, null=True)  # Field name made lowercase.
    disp_avg_30 = models.FloatField(db_column='disp_Avg_30', blank=True, null=True)  # Field name made lowercase.
    disp_avg_31 = models.FloatField(db_column='disp_Avg_31', blank=True, null=True)  # Field name made lowercase.
    disp_avg_32 = models.FloatField(db_column='disp_Avg_32', blank=True, null=True)  # Field name made lowercase.
    laser_avg_1 = models.FloatField(db_column='laser_Avg_1', blank=True, null=True)  # Field name made lowercase.
    laser_avg_2 = models.FloatField(db_column='laser_Avg_2', blank=True, null=True)  # Field name made lowercase.
    laser_avg_3 = models.FloatField(db_column='laser_Avg_3', blank=True, null=True)  # Field name made lowercase.
    temp_f_avg_1 = models.FloatField(db_column='Temp_F_Avg_1', blank=True, null=True)  # Field name made lowercase.
    temp_f_avg_2 = models.FloatField(db_column='Temp_F_Avg_2', blank=True, null=True)  # Field name made lowercase.
    temp_f_avg_3 = models.FloatField(db_column='Temp_F_Avg_3', blank=True, null=True)  # Field name made lowercase.
    ptemp_c_avg = models.FloatField(db_column='PTemp_C_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NY17_Table3'
        unique_together = (('tmstamp', 'recnum'),)


class Ny17Test(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    batt_volt_min = models.FloatField(db_column='Batt_volt_Min', blank=True, null=True)  # Field name made lowercase.
    ptemp = models.FloatField(db_column='PTemp', blank=True, null=True)  # Field name made lowercase.
    laser_18 = models.FloatField(blank=True, null=True)
    laser_19 = models.FloatField(blank=True, null=True)
    laser_29 = models.FloatField(blank=True, null=True)
    laser_40 = models.FloatField(blank=True, null=True)
    thermo_18 = models.FloatField(blank=True, null=True)
    thermo_19 = models.FloatField(blank=True, null=True)
    thermo_29 = models.FloatField(blank=True, null=True)
    thermo_40 = models.FloatField(blank=True, null=True)
    ptemp_c = models.FloatField(db_column='PTemp_C', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NY17_Test'
        unique_together = (('tmstamp', 'recnum'),)


class UvaVsmTable2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    battv_min = models.FloatField(db_column='BattV_Min', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UVA_vsm_Table2'
        unique_together = (('tmstamp', 'recnum'),)


class UvaVsmUvarawreadings(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    diffvolt_avg_1 = models.FloatField(db_column='DiffVolt_Avg_1', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_2 = models.FloatField(db_column='DiffVolt_Avg_2', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_3 = models.FloatField(db_column='DiffVolt_Avg_3', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_4 = models.FloatField(db_column='DiffVolt_Avg_4', blank=True, null=True)  # Field name made lowercase.
    diffvolt_avg_5 = models.FloatField(db_column='DiffVolt_Avg_5', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_1 = models.FloatField(db_column='DiffVolt_2_Avg_1', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_2 = models.FloatField(db_column='DiffVolt_2_Avg_2', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_3 = models.FloatField(db_column='DiffVolt_2_Avg_3', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_4 = models.FloatField(db_column='DiffVolt_2_Avg_4', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_5 = models.FloatField(db_column='DiffVolt_2_Avg_5', blank=True, null=True)  # Field name made lowercase.
    diffvolt_2_avg_6 = models.FloatField(db_column='DiffVolt_2_Avg_6', blank=True, null=True)  # Field name made lowercase.
    therm_c_avg_1 = models.FloatField(db_column='Therm_C_Avg_1', blank=True, null=True)  # Field name made lowercase.
    therm_c_avg_2 = models.FloatField(db_column='Therm_C_Avg_2', blank=True, null=True)  # Field name made lowercase.
    therm_c_avg_3 = models.FloatField(db_column='Therm_C_Avg_3', blank=True, null=True)  # Field name made lowercase.
    therm_c_avg_4 = models.FloatField(db_column='Therm_C_Avg_4', blank=True, null=True)  # Field name made lowercase.
    therm_c_avg_5 = models.FloatField(db_column='Therm_C_Avg_5', blank=True, null=True)  # Field name made lowercase.
    therm_c_2_avg_1 = models.FloatField(db_column='Therm_C_2_Avg_1', blank=True, null=True)  # Field name made lowercase.
    therm_c_2_avg_2 = models.FloatField(db_column='Therm_C_2_Avg_2', blank=True, null=True)  # Field name made lowercase.
    therm_c_2_avg_3 = models.FloatField(db_column='Therm_C_2_Avg_3', blank=True, null=True)  # Field name made lowercase.
    therm_c_2_avg_4 = models.FloatField(db_column='Therm_C_2_Avg_4', blank=True, null=True)  # Field name made lowercase.
    therm_c_2_avg_5 = models.FloatField(db_column='Therm_C_2_Avg_5', blank=True, null=True)  # Field name made lowercase.
    therm_c_2_avg_6 = models.FloatField(db_column='Therm_C_2_Avg_6', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UVA_vsm_UVARawReadings'
        unique_together = (('tmstamp', 'recnum'),)


class DanzPressures(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp')  # Field name made lowercase.
    corner = models.CharField(max_length=15, blank=True, null=True)
    reader = models.CharField(max_length=255, blank=True, null=True)
    measurement = models.FloatField(blank=True, null=True)
    distance = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    phase = models.CharField(max_length=255, blank=True, null=True)
    jack_ht = models.CharField(max_length=255, blank=True, null=True)
    phase_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'danz_pressures'
