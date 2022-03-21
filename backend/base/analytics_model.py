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


class 420Wash4HMedian(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    tilt1_avg = models.FloatField(db_column='Tilt1_Avg', blank=True, null=True)  # Field name made lowercase.
    tilt2_avg = models.FloatField(db_column='Tilt2_Avg', blank=True, null=True)  # Field name made lowercase.
    temptilt1_avg = models.FloatField(db_column='TempTilt1_Avg', blank=True, null=True)  # Field name made lowercase.
    temptilt2_avg = models.FloatField(db_column='TempTilt2_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '420Wash_4H_median'


class Ladot500DtlDMedian(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
    battvoltage = models.FloatField(db_column='battVoltage', blank=True, null=True)  # Field name made lowercase.
    ptemp = models.FloatField(db_column='pTemp', blank=True, null=True)  # Field name made lowercase.
    dtl_1_a = models.FloatField(db_column='DTL-1_A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_1_b = models.FloatField(db_column='DTL-1_B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_2_a = models.FloatField(db_column='DTL-2_A', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dtl_2_b = models.FloatField(db_column='DTL-2_B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'LADOT_500_DTL_D_median'


class Ladot5014HMedian(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'LADOT_501_4H_median'


class Ladot501DayMax(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'LADOT_501_Day_max'


class Ladot501DayMedian(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'LADOT_501_Day_median'


class Ladot501DayMin(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'LADOT_501_Day_min'


class Ladot5024HMedian(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'LADOT_502_4H_median'


class Ladot6014HMedian(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    temp_c_top_avg = models.FloatField(db_column='Temp_C_Top_Avg', blank=True, null=True)  # Field name made lowercase.
    temp_c_bottom_avg = models.FloatField(db_column='Temp_C_Bottom_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_601_4H_median'


class Ladot6024HMedian(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    recnum = models.FloatField(db_column='RecNum', blank=True, null=True)  # Field name made lowercase.
    battv_max = models.FloatField(db_column='BattV_Max', blank=True, null=True)  # Field name made lowercase.
    ptemp_max = models.FloatField(db_column='PTemp_Max', blank=True, null=True)  # Field name made lowercase.
    laser1_med = models.FloatField(db_column='laser1_Med', blank=True, null=True)  # Field name made lowercase.
    laser2_med = models.FloatField(db_column='laser2_Med', blank=True, null=True)  # Field name made lowercase.
    temp_f_ambient_avg = models.FloatField(db_column='Temp_F_Ambient_Avg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_602_4H_median'


class LadotAlltemps4H(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    ambient_temp = models.FloatField(db_column='Ambient_Temp', blank=True, null=True)  # Field name made lowercase.
    deck_bottom_temp = models.FloatField(db_column='Deck_Bottom_Temp', blank=True, null=True)  # Field name made lowercase.
    deck_top_temp = models.FloatField(db_column='Deck_Top_Temp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LADOT_alltemps_4h'


class DanzBearingEast(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    sensor_0_banda = models.FloatField(db_column='Sensor_0_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_1_banda = models.FloatField(db_column='Sensor_1_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_2_banda = models.FloatField(db_column='Sensor_2_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_3_banda = models.FloatField(db_column='Sensor_3_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_4_banda = models.FloatField(db_column='Sensor_4_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_5_banda = models.FloatField(db_column='Sensor_5_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_6_banda = models.FloatField(db_column='Sensor_6_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_7_banda = models.FloatField(db_column='Sensor_7_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_8_banda = models.FloatField(db_column='Sensor_8_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_9_banda = models.FloatField(db_column='Sensor_9_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_10_banda = models.FloatField(db_column='Sensor_10_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_11_banda = models.FloatField(db_column='Sensor_11_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_12_banda = models.FloatField(db_column='Sensor_12_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_13_banda = models.FloatField(db_column='Sensor_13_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_14_banda = models.FloatField(db_column='Sensor_14_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_15_banda = models.FloatField(db_column='Sensor_15_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandb = models.FloatField(db_column='Sensor_0_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandb = models.FloatField(db_column='Sensor_1_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandb = models.FloatField(db_column='Sensor_2_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandb = models.FloatField(db_column='Sensor_3_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandb = models.FloatField(db_column='Sensor_4_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandb = models.FloatField(db_column='Sensor_5_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandb = models.FloatField(db_column='Sensor_6_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandb = models.FloatField(db_column='Sensor_7_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandb = models.FloatField(db_column='Sensor_8_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandb = models.FloatField(db_column='Sensor_9_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandb = models.FloatField(db_column='Sensor_10_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandb = models.FloatField(db_column='Sensor_11_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandb = models.FloatField(db_column='Sensor_12_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandb = models.FloatField(db_column='Sensor_13_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandb = models.FloatField(db_column='Sensor_14_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandb = models.FloatField(db_column='Sensor_15_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandc = models.FloatField(db_column='Sensor_0_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandc = models.FloatField(db_column='Sensor_1_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandc = models.FloatField(db_column='Sensor_2_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandc = models.FloatField(db_column='Sensor_3_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandc = models.FloatField(db_column='Sensor_4_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandc = models.FloatField(db_column='Sensor_5_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandc = models.FloatField(db_column='Sensor_6_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandc = models.FloatField(db_column='Sensor_7_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandc = models.FloatField(db_column='Sensor_8_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandc = models.FloatField(db_column='Sensor_9_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandc = models.FloatField(db_column='Sensor_10_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandc = models.FloatField(db_column='Sensor_11_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandc = models.FloatField(db_column='Sensor_12_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandc = models.FloatField(db_column='Sensor_13_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandc = models.FloatField(db_column='Sensor_14_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandc = models.FloatField(db_column='Sensor_15_BandC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_bearing_east'


class DanzBearingEast2(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    sensor_0_banda = models.FloatField(db_column='Sensor_0_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_1_banda = models.FloatField(db_column='Sensor_1_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_2_banda = models.FloatField(db_column='Sensor_2_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_3_banda = models.FloatField(db_column='Sensor_3_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_4_banda = models.FloatField(db_column='Sensor_4_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_5_banda = models.FloatField(db_column='Sensor_5_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_6_banda = models.FloatField(db_column='Sensor_6_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_7_banda = models.FloatField(db_column='Sensor_7_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_8_banda = models.FloatField(db_column='Sensor_8_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_9_banda = models.FloatField(db_column='Sensor_9_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_10_banda = models.FloatField(db_column='Sensor_10_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_11_banda = models.FloatField(db_column='Sensor_11_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_12_banda = models.FloatField(db_column='Sensor_12_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_13_banda = models.FloatField(db_column='Sensor_13_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_14_banda = models.FloatField(db_column='Sensor_14_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_15_banda = models.FloatField(db_column='Sensor_15_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandb = models.FloatField(db_column='Sensor_0_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandb = models.FloatField(db_column='Sensor_1_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandb = models.FloatField(db_column='Sensor_2_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandb = models.FloatField(db_column='Sensor_3_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandb = models.FloatField(db_column='Sensor_4_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandb = models.FloatField(db_column='Sensor_5_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandb = models.FloatField(db_column='Sensor_6_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandb = models.FloatField(db_column='Sensor_7_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandb = models.FloatField(db_column='Sensor_8_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandb = models.FloatField(db_column='Sensor_9_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandb = models.FloatField(db_column='Sensor_10_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandb = models.FloatField(db_column='Sensor_11_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandb = models.FloatField(db_column='Sensor_12_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandb = models.FloatField(db_column='Sensor_13_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandb = models.FloatField(db_column='Sensor_14_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandb = models.FloatField(db_column='Sensor_15_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandc = models.FloatField(db_column='Sensor_0_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandc = models.FloatField(db_column='Sensor_1_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandc = models.FloatField(db_column='Sensor_2_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandc = models.FloatField(db_column='Sensor_3_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandc = models.FloatField(db_column='Sensor_4_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandc = models.FloatField(db_column='Sensor_5_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandc = models.FloatField(db_column='Sensor_6_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandc = models.FloatField(db_column='Sensor_7_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandc = models.FloatField(db_column='Sensor_8_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandc = models.FloatField(db_column='Sensor_9_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandc = models.FloatField(db_column='Sensor_10_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandc = models.FloatField(db_column='Sensor_11_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandc = models.FloatField(db_column='Sensor_12_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandc = models.FloatField(db_column='Sensor_13_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandc = models.FloatField(db_column='Sensor_14_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandc = models.FloatField(db_column='Sensor_15_BandC', blank=True, null=True)  # Field name made lowercase.
    valid = models.BooleanField(db_column='Valid', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_bearing_east2'


class DanzBearingLimits(models.Model):
    limit = models.TextField(blank=True, null=True)
    sensor_0_banda = models.FloatField(db_column='Sensor_0_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_1_banda = models.FloatField(db_column='Sensor_1_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_2_banda = models.FloatField(db_column='Sensor_2_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_3_banda = models.FloatField(db_column='Sensor_3_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_4_banda = models.FloatField(db_column='Sensor_4_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_5_banda = models.FloatField(db_column='Sensor_5_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_6_banda = models.FloatField(db_column='Sensor_6_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_7_banda = models.FloatField(db_column='Sensor_7_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_8_banda = models.FloatField(db_column='Sensor_8_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_9_banda = models.FloatField(db_column='Sensor_9_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_10_banda = models.FloatField(db_column='Sensor_10_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_11_banda = models.FloatField(db_column='Sensor_11_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_12_banda = models.FloatField(db_column='Sensor_12_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_13_banda = models.FloatField(db_column='Sensor_13_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_14_banda = models.FloatField(db_column='Sensor_14_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_15_banda = models.FloatField(db_column='Sensor_15_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandb = models.FloatField(db_column='Sensor_0_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandb = models.FloatField(db_column='Sensor_1_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandb = models.FloatField(db_column='Sensor_2_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandb = models.FloatField(db_column='Sensor_3_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandb = models.FloatField(db_column='Sensor_4_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandb = models.FloatField(db_column='Sensor_5_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandb = models.FloatField(db_column='Sensor_6_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandb = models.FloatField(db_column='Sensor_7_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandb = models.FloatField(db_column='Sensor_8_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandb = models.FloatField(db_column='Sensor_9_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandb = models.FloatField(db_column='Sensor_10_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandb = models.FloatField(db_column='Sensor_11_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandb = models.FloatField(db_column='Sensor_12_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandb = models.FloatField(db_column='Sensor_13_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandb = models.FloatField(db_column='Sensor_14_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandb = models.FloatField(db_column='Sensor_15_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandc = models.FloatField(db_column='Sensor_0_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandc = models.FloatField(db_column='Sensor_1_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandc = models.FloatField(db_column='Sensor_2_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandc = models.FloatField(db_column='Sensor_3_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandc = models.FloatField(db_column='Sensor_4_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandc = models.FloatField(db_column='Sensor_5_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandc = models.FloatField(db_column='Sensor_6_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandc = models.FloatField(db_column='Sensor_7_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandc = models.FloatField(db_column='Sensor_8_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandc = models.FloatField(db_column='Sensor_9_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandc = models.FloatField(db_column='Sensor_10_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandc = models.FloatField(db_column='Sensor_11_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandc = models.FloatField(db_column='Sensor_12_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandc = models.FloatField(db_column='Sensor_13_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandc = models.FloatField(db_column='Sensor_14_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandc = models.FloatField(db_column='Sensor_15_BandC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_bearing_limits'


class DanzBearingWest(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    sensor_0_banda = models.FloatField(db_column='Sensor_0_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_1_banda = models.FloatField(db_column='Sensor_1_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_2_banda = models.FloatField(db_column='Sensor_2_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_3_banda = models.FloatField(db_column='Sensor_3_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_4_banda = models.FloatField(db_column='Sensor_4_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_5_banda = models.FloatField(db_column='Sensor_5_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_6_banda = models.FloatField(db_column='Sensor_6_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_7_banda = models.FloatField(db_column='Sensor_7_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_8_banda = models.FloatField(db_column='Sensor_8_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_9_banda = models.FloatField(db_column='Sensor_9_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_10_banda = models.FloatField(db_column='Sensor_10_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_11_banda = models.FloatField(db_column='Sensor_11_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_12_banda = models.FloatField(db_column='Sensor_12_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_13_banda = models.FloatField(db_column='Sensor_13_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_14_banda = models.FloatField(db_column='Sensor_14_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_15_banda = models.FloatField(db_column='Sensor_15_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandb = models.FloatField(db_column='Sensor_0_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandb = models.FloatField(db_column='Sensor_1_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandb = models.FloatField(db_column='Sensor_2_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandb = models.FloatField(db_column='Sensor_3_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandb = models.FloatField(db_column='Sensor_4_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandb = models.FloatField(db_column='Sensor_5_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandb = models.FloatField(db_column='Sensor_6_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandb = models.FloatField(db_column='Sensor_7_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandb = models.FloatField(db_column='Sensor_8_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandb = models.FloatField(db_column='Sensor_9_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandb = models.FloatField(db_column='Sensor_10_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandb = models.FloatField(db_column='Sensor_11_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandb = models.FloatField(db_column='Sensor_12_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandb = models.FloatField(db_column='Sensor_13_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandb = models.FloatField(db_column='Sensor_14_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandb = models.FloatField(db_column='Sensor_15_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandc = models.FloatField(db_column='Sensor_0_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandc = models.FloatField(db_column='Sensor_1_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandc = models.FloatField(db_column='Sensor_2_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandc = models.FloatField(db_column='Sensor_3_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandc = models.FloatField(db_column='Sensor_4_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandc = models.FloatField(db_column='Sensor_5_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandc = models.FloatField(db_column='Sensor_6_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandc = models.FloatField(db_column='Sensor_7_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandc = models.FloatField(db_column='Sensor_8_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandc = models.FloatField(db_column='Sensor_9_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandc = models.FloatField(db_column='Sensor_10_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandc = models.FloatField(db_column='Sensor_11_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandc = models.FloatField(db_column='Sensor_12_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandc = models.FloatField(db_column='Sensor_13_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandc = models.FloatField(db_column='Sensor_14_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandc = models.FloatField(db_column='Sensor_15_BandC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_bearing_west'


class DanzBearingWest2(models.Model):
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(primary_key=True)
    sensor_0_banda = models.FloatField(db_column='Sensor_0_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_1_banda = models.FloatField(db_column='Sensor_1_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_2_banda = models.FloatField(db_column='Sensor_2_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_3_banda = models.FloatField(db_column='Sensor_3_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_4_banda = models.FloatField(db_column='Sensor_4_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_5_banda = models.FloatField(db_column='Sensor_5_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_6_banda = models.FloatField(db_column='Sensor_6_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_7_banda = models.FloatField(db_column='Sensor_7_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_8_banda = models.FloatField(db_column='Sensor_8_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_9_banda = models.FloatField(db_column='Sensor_9_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_10_banda = models.FloatField(db_column='Sensor_10_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_11_banda = models.FloatField(db_column='Sensor_11_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_12_banda = models.FloatField(db_column='Sensor_12_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_13_banda = models.FloatField(db_column='Sensor_13_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_14_banda = models.FloatField(db_column='Sensor_14_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_15_banda = models.FloatField(db_column='Sensor_15_BandA', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandb = models.FloatField(db_column='Sensor_0_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandb = models.FloatField(db_column='Sensor_1_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandb = models.FloatField(db_column='Sensor_2_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandb = models.FloatField(db_column='Sensor_3_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandb = models.FloatField(db_column='Sensor_4_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandb = models.FloatField(db_column='Sensor_5_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandb = models.FloatField(db_column='Sensor_6_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandb = models.FloatField(db_column='Sensor_7_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandb = models.FloatField(db_column='Sensor_8_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandb = models.FloatField(db_column='Sensor_9_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandb = models.FloatField(db_column='Sensor_10_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandb = models.FloatField(db_column='Sensor_11_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandb = models.FloatField(db_column='Sensor_12_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandb = models.FloatField(db_column='Sensor_13_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandb = models.FloatField(db_column='Sensor_14_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandb = models.FloatField(db_column='Sensor_15_BandB', blank=True, null=True)  # Field name made lowercase.
    sensor_0_bandc = models.FloatField(db_column='Sensor_0_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_1_bandc = models.FloatField(db_column='Sensor_1_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_2_bandc = models.FloatField(db_column='Sensor_2_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_3_bandc = models.FloatField(db_column='Sensor_3_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_4_bandc = models.FloatField(db_column='Sensor_4_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_5_bandc = models.FloatField(db_column='Sensor_5_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_6_bandc = models.FloatField(db_column='Sensor_6_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_7_bandc = models.FloatField(db_column='Sensor_7_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_8_bandc = models.FloatField(db_column='Sensor_8_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_9_bandc = models.FloatField(db_column='Sensor_9_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_10_bandc = models.FloatField(db_column='Sensor_10_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_11_bandc = models.FloatField(db_column='Sensor_11_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_12_bandc = models.FloatField(db_column='Sensor_12_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_13_bandc = models.FloatField(db_column='Sensor_13_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_14_bandc = models.FloatField(db_column='Sensor_14_BandC', blank=True, null=True)  # Field name made lowercase.
    sensor_15_bandc = models.FloatField(db_column='Sensor_15_BandC', blank=True, null=True)  # Field name made lowercase.
    valid = models.BooleanField(db_column='Valid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_bearing_west2'


class DanzLifts(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    verified = models.BooleanField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'danz_lifts'


class DanzResensyWide1Min(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    t21_top = models.FloatField(db_column='T21_Top', blank=True, null=True)  # Field name made lowercase.
    t21_bot = models.FloatField(db_column='T21_Bot', blank=True, null=True)  # Field name made lowercase.
    t21_in = models.FloatField(db_column='T21_In', blank=True, null=True)  # Field name made lowercase.
    t21_out = models.FloatField(db_column='T21_Out', blank=True, null=True)  # Field name made lowercase.
    t22_bot = models.FloatField(db_column='T22_Bot', blank=True, null=True)  # Field name made lowercase.
    t22_in = models.FloatField(db_column='T22_In', blank=True, null=True)  # Field name made lowercase.
    t22s_top = models.FloatField(db_column='T22S_Top', blank=True, null=True)  # Field name made lowercase.
    t22s_bot = models.FloatField(db_column='T22S_Bot', blank=True, null=True)  # Field name made lowercase.
    t22s_in = models.FloatField(db_column='T22S_In', blank=True, null=True)  # Field name made lowercase.
    t22s_out = models.FloatField(db_column='T22S_Out', blank=True, null=True)  # Field name made lowercase.
    t23_top = models.FloatField(db_column='T23_Top', blank=True, null=True)  # Field name made lowercase.
    t23_bot = models.FloatField(db_column='T23_Bot', blank=True, null=True)  # Field name made lowercase.
    t23_in = models.FloatField(db_column='T23_In', blank=True, null=True)  # Field name made lowercase.
    t23_out = models.FloatField(db_column='T23_Out', blank=True, null=True)  # Field name made lowercase.
    l22_21_top = models.FloatField(db_column='L22_21_Top', blank=True, null=True)  # Field name made lowercase.
    l22_21_bot = models.FloatField(db_column='L22_21_Bot', blank=True, null=True)  # Field name made lowercase.
    l22_21_east = models.FloatField(db_column='L22_21_East', blank=True, null=True)  # Field name made lowercase.
    l22_21_west = models.FloatField(db_column='L22_21_West', blank=True, null=True)  # Field name made lowercase.
    l22_23_top = models.FloatField(db_column='L22_23_Top', blank=True, null=True)  # Field name made lowercase.
    l22_23_bot = models.FloatField(db_column='L22_23_Bot', blank=True, null=True)  # Field name made lowercase.
    l22_23_east = models.FloatField(db_column='L22_23_East', blank=True, null=True)  # Field name made lowercase.
    l22_23_west = models.FloatField(db_column='L22_23_West', blank=True, null=True)  # Field name made lowercase.
    t21_top_temp = models.FloatField(db_column='T21_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t21_bot_temp = models.FloatField(db_column='T21_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t21_in_temp = models.FloatField(db_column='T21_In_temp', blank=True, null=True)  # Field name made lowercase.
    t21_out_temp = models.FloatField(db_column='T21_Out_temp', blank=True, null=True)  # Field name made lowercase.
    t22_bot_temp = models.FloatField(db_column='T22_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t22_in_temp = models.FloatField(db_column='T22_In_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_top_temp = models.FloatField(db_column='T22S_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_bot_temp = models.FloatField(db_column='T22S_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_in_temp = models.FloatField(db_column='T22S_In_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_out_temp = models.FloatField(db_column='T22S_Out_temp', blank=True, null=True)  # Field name made lowercase.
    t23_top_temp = models.FloatField(db_column='T23_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t23_bot_temp = models.FloatField(db_column='T23_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t23_in_temp = models.FloatField(db_column='T23_In_temp', blank=True, null=True)  # Field name made lowercase.
    t23_out_temp = models.FloatField(db_column='T23_Out_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_top_temp = models.FloatField(db_column='L22_21_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_bot_temp = models.FloatField(db_column='L22_21_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_east_temp = models.FloatField(db_column='L22_21_East_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_west_temp = models.FloatField(db_column='L22_21_West_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_top_temp = models.FloatField(db_column='L22_23_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_bot_temp = models.FloatField(db_column='L22_23_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_east_temp = models.FloatField(db_column='L22_23_East_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_west_temp = models.FloatField(db_column='L22_23_West_temp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_resensy_wide_1min'


class DanzResensyWide1MinForces2(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    l18_19 = models.FloatField(db_column='L18_19', blank=True, null=True)  # Field name made lowercase.
    l22_21 = models.FloatField(db_column='L22_21', blank=True, null=True)  # Field name made lowercase.
    l22_23 = models.FloatField(db_column='L22_23', blank=True, null=True)  # Field name made lowercase.
    l24_25 = models.FloatField(db_column='L24_25', blank=True, null=True)  # Field name made lowercase.
    t20 = models.FloatField(db_column='T20', blank=True, null=True)  # Field name made lowercase.
    t22s = models.FloatField(db_column='T22S', blank=True, null=True)  # Field name made lowercase.
    t23 = models.FloatField(db_column='T23', blank=True, null=True)  # Field name made lowercase.
    t24_25 = models.FloatField(db_column='T24_25', blank=True, null=True)  # Field name made lowercase.
    arch = models.FloatField(db_column='Arch', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_resensy_wide_1min_forces2'


class DanzResensyWide1MinStrain(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    t21_top = models.FloatField(db_column='T21_Top', blank=True, null=True)  # Field name made lowercase.
    t21_bot = models.FloatField(db_column='T21_Bot', blank=True, null=True)  # Field name made lowercase.
    t21_in = models.FloatField(db_column='T21_In', blank=True, null=True)  # Field name made lowercase.
    t21_out = models.FloatField(db_column='T21_Out', blank=True, null=True)  # Field name made lowercase.
    t22_bot = models.FloatField(db_column='T22_Bot', blank=True, null=True)  # Field name made lowercase.
    t22_in = models.FloatField(db_column='T22_In', blank=True, null=True)  # Field name made lowercase.
    t22s_top = models.FloatField(db_column='T22S_Top', blank=True, null=True)  # Field name made lowercase.
    t22s_bot = models.FloatField(db_column='T22S_Bot', blank=True, null=True)  # Field name made lowercase.
    t22s_in = models.FloatField(db_column='T22S_In', blank=True, null=True)  # Field name made lowercase.
    t22s_out = models.FloatField(db_column='T22S_Out', blank=True, null=True)  # Field name made lowercase.
    t23_top = models.FloatField(db_column='T23_Top', blank=True, null=True)  # Field name made lowercase.
    t23_bot = models.FloatField(db_column='T23_Bot', blank=True, null=True)  # Field name made lowercase.
    t23_in = models.FloatField(db_column='T23_In', blank=True, null=True)  # Field name made lowercase.
    t23_out = models.FloatField(db_column='T23_Out', blank=True, null=True)  # Field name made lowercase.
    l22_21_top = models.FloatField(db_column='L22_21_Top', blank=True, null=True)  # Field name made lowercase.
    l22_21_bot = models.FloatField(db_column='L22_21_Bot', blank=True, null=True)  # Field name made lowercase.
    l22_21_east = models.FloatField(db_column='L22_21_East', blank=True, null=True)  # Field name made lowercase.
    l22_21_west = models.FloatField(db_column='L22_21_West', blank=True, null=True)  # Field name made lowercase.
    l22_23_top = models.FloatField(db_column='L22_23_Top', blank=True, null=True)  # Field name made lowercase.
    l22_23_bot = models.FloatField(db_column='L22_23_Bot', blank=True, null=True)  # Field name made lowercase.
    l22_23_east = models.FloatField(db_column='L22_23_East', blank=True, null=True)  # Field name made lowercase.
    l22_23_west = models.FloatField(db_column='L22_23_West', blank=True, null=True)  # Field name made lowercase.
    a_bot = models.FloatField(db_column='A_Bot', blank=True, null=True)  # Field name made lowercase.
    a_nf = models.FloatField(db_column='A_NF', blank=True, null=True)  # Field name made lowercase.
    a_sf = models.FloatField(db_column='A_SF', blank=True, null=True)  # Field name made lowercase.
    a_top = models.FloatField(db_column='A_Top', blank=True, null=True)  # Field name made lowercase.
    t20_bot = models.FloatField(db_column='T20_Bot', blank=True, null=True)  # Field name made lowercase.
    t20_nf = models.FloatField(db_column='T20_NF', blank=True, null=True)  # Field name made lowercase.
    t20_sf = models.FloatField(db_column='T20_SF', blank=True, null=True)  # Field name made lowercase.
    t20_top = models.FloatField(db_column='T20_Top', blank=True, null=True)  # Field name made lowercase.
    t22_w5_in = models.FloatField(db_column='T22_W5_In', blank=True, null=True)  # Field name made lowercase.
    t22_w5_out = models.FloatField(db_column='T22_W5_Out', blank=True, null=True)  # Field name made lowercase.
    l18_19_bot = models.FloatField(db_column='L18_19_Bot', blank=True, null=True)  # Field name made lowercase.
    l18_19_east = models.FloatField(db_column='L18_19_East', blank=True, null=True)  # Field name made lowercase.
    l18_19_top = models.FloatField(db_column='L18_19_Top', blank=True, null=True)  # Field name made lowercase.
    l18_19_west = models.FloatField(db_column='L18_19_West', blank=True, null=True)  # Field name made lowercase.
    l24_25_bot = models.FloatField(db_column='L24_25_Bot', blank=True, null=True)  # Field name made lowercase.
    l24_25_top = models.FloatField(db_column='L24_25_Top', blank=True, null=True)  # Field name made lowercase.
    l24_25_east = models.FloatField(db_column='L24_25_East', blank=True, null=True)  # Field name made lowercase.
    l24_25_west = models.FloatField(db_column='L24_25_West', blank=True, null=True)  # Field name made lowercase.
    t24_25_in = models.FloatField(db_column='T24_25_In', blank=True, null=True)  # Field name made lowercase.
    t24_25_bot = models.FloatField(db_column='T24_25_Bot', blank=True, null=True)  # Field name made lowercase.
    t24_25_top = models.FloatField(db_column='T24_25_Top', blank=True, null=True)  # Field name made lowercase.
    t24_25n_out = models.FloatField(db_column='T24_25N_Out', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_resensy_wide_1min_strain'


class DanzResensyWide1MinStrain2(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    t22s_top = models.FloatField(db_column='T22S_Top', blank=True, null=True)  # Field name made lowercase.
    t22s_bot = models.FloatField(db_column='T22S_Bot', blank=True, null=True)  # Field name made lowercase.
    t22s_in = models.FloatField(db_column='T22S_In', blank=True, null=True)  # Field name made lowercase.
    t22s_out = models.FloatField(db_column='T22S_Out', blank=True, null=True)  # Field name made lowercase.
    t23_top = models.FloatField(db_column='T23_Top', blank=True, null=True)  # Field name made lowercase.
    t23_bot = models.FloatField(db_column='T23_Bot', blank=True, null=True)  # Field name made lowercase.
    t23_in = models.FloatField(db_column='T23_In', blank=True, null=True)  # Field name made lowercase.
    t23_out = models.FloatField(db_column='T23_Out', blank=True, null=True)  # Field name made lowercase.
    l22_21_top = models.FloatField(db_column='L22_21_Top', blank=True, null=True)  # Field name made lowercase.
    l22_21_bot = models.FloatField(db_column='L22_21_Bot', blank=True, null=True)  # Field name made lowercase.
    l22_21_east = models.FloatField(db_column='L22_21_East', blank=True, null=True)  # Field name made lowercase.
    l22_21_west = models.FloatField(db_column='L22_21_West', blank=True, null=True)  # Field name made lowercase.
    l22_23_top = models.FloatField(db_column='L22_23_Top', blank=True, null=True)  # Field name made lowercase.
    l22_23_bot = models.FloatField(db_column='L22_23_Bot', blank=True, null=True)  # Field name made lowercase.
    l22_23_east = models.FloatField(db_column='L22_23_East', blank=True, null=True)  # Field name made lowercase.
    l22_23_west = models.FloatField(db_column='L22_23_West', blank=True, null=True)  # Field name made lowercase.
    a_bot = models.FloatField(db_column='A_Bot', blank=True, null=True)  # Field name made lowercase.
    a_nf = models.FloatField(db_column='A_NF', blank=True, null=True)  # Field name made lowercase.
    a_sf = models.FloatField(db_column='A_SF', blank=True, null=True)  # Field name made lowercase.
    a_top = models.FloatField(db_column='A_Top', blank=True, null=True)  # Field name made lowercase.
    t20_bot = models.FloatField(db_column='T20_Bot', blank=True, null=True)  # Field name made lowercase.
    t20_nf = models.FloatField(db_column='T20_NF', blank=True, null=True)  # Field name made lowercase.
    t20_sf = models.FloatField(db_column='T20_SF', blank=True, null=True)  # Field name made lowercase.
    t20_top = models.FloatField(db_column='T20_Top', blank=True, null=True)  # Field name made lowercase.
    t23_in_rp = models.FloatField(db_column='T23_In_RP', blank=True, null=True)  # Field name made lowercase.
    t23_out_rp = models.FloatField(db_column='T23_Out_RP', blank=True, null=True)  # Field name made lowercase.
    l18_19_bot = models.FloatField(db_column='L18_19_Bot', blank=True, null=True)  # Field name made lowercase.
    l18_19_east = models.FloatField(db_column='L18_19_East', blank=True, null=True)  # Field name made lowercase.
    l18_19_top = models.FloatField(db_column='L18_19_Top', blank=True, null=True)  # Field name made lowercase.
    l18_19_west = models.FloatField(db_column='L18_19_West', blank=True, null=True)  # Field name made lowercase.
    l24_25_bot = models.FloatField(db_column='L24_25_Bot', blank=True, null=True)  # Field name made lowercase.
    l24_25_top = models.FloatField(db_column='L24_25_Top', blank=True, null=True)  # Field name made lowercase.
    l24_25_east = models.FloatField(db_column='L24_25_East', blank=True, null=True)  # Field name made lowercase.
    l24_25_west = models.FloatField(db_column='L24_25_West', blank=True, null=True)  # Field name made lowercase.
    t24_25_in = models.FloatField(db_column='T24_25_In', blank=True, null=True)  # Field name made lowercase.
    t24_25_bot = models.FloatField(db_column='T24_25_Bot', blank=True, null=True)  # Field name made lowercase.
    t24_25_top = models.FloatField(db_column='T24_25_Top', blank=True, null=True)  # Field name made lowercase.
    t24_25n_out = models.FloatField(db_column='T24_25N_Out', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_resensy_wide_1min_strain2'


class DanzResensyWide1MinTemp(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    t21_top_temp = models.FloatField(db_column='T21_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t21_bot_temp = models.FloatField(db_column='T21_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t21_in_temp = models.FloatField(db_column='T21_In_temp', blank=True, null=True)  # Field name made lowercase.
    t21_out_temp = models.FloatField(db_column='T21_Out_temp', blank=True, null=True)  # Field name made lowercase.
    t22_bot_temp = models.FloatField(db_column='T22_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t22_in_temp = models.FloatField(db_column='T22_In_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_top_temp = models.FloatField(db_column='T22S_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_bot_temp = models.FloatField(db_column='T22S_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_in_temp = models.FloatField(db_column='T22S_In_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_out_temp = models.FloatField(db_column='T22S_Out_temp', blank=True, null=True)  # Field name made lowercase.
    t23_top_temp = models.FloatField(db_column='T23_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t23_bot_temp = models.FloatField(db_column='T23_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t23_in_temp = models.FloatField(db_column='T23_In_temp', blank=True, null=True)  # Field name made lowercase.
    t23_out_temp = models.FloatField(db_column='T23_Out_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_top_temp = models.FloatField(db_column='L22_21_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_bot_temp = models.FloatField(db_column='L22_21_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_east_temp = models.FloatField(db_column='L22_21_East_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_west_temp = models.FloatField(db_column='L22_21_West_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_top_temp = models.FloatField(db_column='L22_23_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_bot_temp = models.FloatField(db_column='L22_23_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_east_temp = models.FloatField(db_column='L22_23_East_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_west_temp = models.FloatField(db_column='L22_23_West_temp', blank=True, null=True)  # Field name made lowercase.
    a_bot_temp = models.FloatField(db_column='A_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    a_nf_temp = models.FloatField(db_column='A_NF_temp', blank=True, null=True)  # Field name made lowercase.
    a_sf_temp = models.FloatField(db_column='A_SF_temp', blank=True, null=True)  # Field name made lowercase.
    a_top_temp = models.FloatField(db_column='A_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t20_bot_temp = models.FloatField(db_column='T20_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t20_nf_temp = models.FloatField(db_column='T20_NF_temp', blank=True, null=True)  # Field name made lowercase.
    t20_sf_temp = models.FloatField(db_column='T20_SF_temp', blank=True, null=True)  # Field name made lowercase.
    t20_top_temp = models.FloatField(db_column='T20_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t22_w5_in_temp = models.FloatField(db_column='T22_W5_In_temp', blank=True, null=True)  # Field name made lowercase.
    t22_w5_out_temp = models.FloatField(db_column='T22_W5_Out_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_bot_temp = models.FloatField(db_column='L18_19_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_east_temp = models.FloatField(db_column='L18_19_East_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_top_temp = models.FloatField(db_column='L18_19_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_west_temp = models.FloatField(db_column='L18_19_West_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_bot_temp = models.FloatField(db_column='L24_25_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_top_temp = models.FloatField(db_column='L24_25_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_east_temp = models.FloatField(db_column='L24_25_East_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_west_temp = models.FloatField(db_column='L24_25_West_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25_in_temp = models.FloatField(db_column='T24_25_In_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25_bot_temp = models.FloatField(db_column='T24_25_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25_top_temp = models.FloatField(db_column='T24_25_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25n_out_temp = models.FloatField(db_column='T24_25N_Out_temp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_resensy_wide_1min_temp'


class DanzResensyWide1MinTemp2(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    t22s_top_temp = models.FloatField(db_column='T22S_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_bot_temp = models.FloatField(db_column='T22S_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_in_temp = models.FloatField(db_column='T22S_In_temp', blank=True, null=True)  # Field name made lowercase.
    t22s_out_temp = models.FloatField(db_column='T22S_Out_temp', blank=True, null=True)  # Field name made lowercase.
    t23_top_temp = models.FloatField(db_column='T23_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t23_bot_temp = models.FloatField(db_column='T23_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t23_in_temp = models.FloatField(db_column='T23_In_temp', blank=True, null=True)  # Field name made lowercase.
    t23_out_temp = models.FloatField(db_column='T23_Out_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_top_temp = models.FloatField(db_column='L22_21_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_bot_temp = models.FloatField(db_column='L22_21_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_east_temp = models.FloatField(db_column='L22_21_East_temp', blank=True, null=True)  # Field name made lowercase.
    l22_21_west_temp = models.FloatField(db_column='L22_21_West_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_top_temp = models.FloatField(db_column='L22_23_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_bot_temp = models.FloatField(db_column='L22_23_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_east_temp = models.FloatField(db_column='L22_23_East_temp', blank=True, null=True)  # Field name made lowercase.
    l22_23_west_temp = models.FloatField(db_column='L22_23_West_temp', blank=True, null=True)  # Field name made lowercase.
    a_bot_temp = models.FloatField(db_column='A_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    a_nf_temp = models.FloatField(db_column='A_NF_temp', blank=True, null=True)  # Field name made lowercase.
    a_sf_temp = models.FloatField(db_column='A_SF_temp', blank=True, null=True)  # Field name made lowercase.
    a_top_temp = models.FloatField(db_column='A_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t20_bot_temp = models.FloatField(db_column='T20_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t20_nf_temp = models.FloatField(db_column='T20_NF_temp', blank=True, null=True)  # Field name made lowercase.
    t20_sf_temp = models.FloatField(db_column='T20_SF_temp', blank=True, null=True)  # Field name made lowercase.
    t20_top_temp = models.FloatField(db_column='T20_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t23_in_rp_temp = models.FloatField(db_column='T23_In_RP_temp', blank=True, null=True)  # Field name made lowercase.
    t23_out_rp_temp = models.FloatField(db_column='T23_Out_RP_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_bot_temp = models.FloatField(db_column='L18_19_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_east_temp = models.FloatField(db_column='L18_19_East_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_top_temp = models.FloatField(db_column='L18_19_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l18_19_west_temp = models.FloatField(db_column='L18_19_West_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_bot_temp = models.FloatField(db_column='L24_25_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_top_temp = models.FloatField(db_column='L24_25_Top_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_east_temp = models.FloatField(db_column='L24_25_East_temp', blank=True, null=True)  # Field name made lowercase.
    l24_25_west_temp = models.FloatField(db_column='L24_25_West_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25_in_temp = models.FloatField(db_column='T24_25_In_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25_bot_temp = models.FloatField(db_column='T24_25_Bot_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25_top_temp = models.FloatField(db_column='T24_25_Top_temp', blank=True, null=True)  # Field name made lowercase.
    t24_25n_out_temp = models.FloatField(db_column='T24_25N_Out_temp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'danz_resensy_wide_1min_temp2'


class DanzUltraRaw(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    sensorname = models.CharField(max_length=50, blank=True, null=True)
    sensordata = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'danz_ultra_raw'


class DboUvaTiltRaw(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    sensorname = models.TextField(blank=True, null=True)
    sensordata = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dbo.uva_tilt_raw'


class EastD001(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    ggq = models.TextField(db_column='GGQ', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(blank=True, null=True)
    ns = models.TextField(db_column='NS', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    ew = models.TextField(db_column='EW', blank=True, null=True)  # Field name made lowercase.
    gps = models.BigIntegerField(blank=True, null=True)
    sat = models.BigIntegerField(blank=True, null=True)
    qc = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    alt_ft = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'east_d001'


class EastD001Day(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    gps = models.BigIntegerField(blank=True, null=True)
    sat = models.FloatField(blank=True, null=True)
    qc = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    alt_ft = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'east_d001_day'


class I40DsiTest(models.Model):
    stepid = models.FloatField()
    stepname = models.CharField(max_length=50, blank=True, null=True)
    p1_f_kips = models.FloatField(db_column='P1_F_kips', blank=True, null=True)  # Field name made lowercase.
    p2_f_kips = models.FloatField(db_column='P2_F_kips', blank=True, null=True)  # Field name made lowercase.
    p3_f_kips = models.FloatField(db_column='P3_F_kips', blank=True, null=True)  # Field name made lowercase.
    p4_f_kips = models.FloatField(db_column='P4_F_kips', blank=True, null=True)  # Field name made lowercase.
    p5_f_kips = models.FloatField(db_column='P5_F_kips', blank=True, null=True)  # Field name made lowercase.
    p6_f_kips = models.FloatField(db_column='P6_F_kips', blank=True, null=True)  # Field name made lowercase.
    p7_f_kips = models.FloatField(db_column='P7_F_kips', blank=True, null=True)  # Field name made lowercase.
    p8_f_kips = models.FloatField(db_column='P8_F_kips', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i40_dsi_test'


class I40ForceTest(models.Model):
    stepid = models.FloatField(primary_key=True)
    sensorname = models.CharField(max_length=50)
    stepname = models.CharField(max_length=50, blank=True, null=True)
    sensorvalue = models.FloatField(blank=True, null=True)
    sensorvalue_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i40_force_test'
        unique_together = (('stepid', 'sensorname'),)


class I40ResensysRaw(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    sensorname = models.CharField(max_length=50)
    sensordata = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i40_resensys_raw'
        unique_together = (('timestamp', 'sensorname'),)


class I40StrainTest(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    stepid = models.FloatField()
    sensorname = models.CharField(max_length=50)
    stepname = models.CharField(max_length=50, blank=True, null=True)
    sensorvalue = models.FloatField(blank=True, null=True)
    sensorvalue_ts = models.DateTimeField(blank=True, null=True)
    tempvalue = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i40_strain_test'
        unique_together = (('timestamp', 'stepid', 'sensorname'),)


class I40TestRecord(models.Model):
    stepid = models.FloatField(db_column='StepID', blank=True, null=True)  # Field name made lowercase.
    stepname = models.TextField(db_column='StepName', blank=True, null=True)  # Field name made lowercase.
    record_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i40_test_record'


class I40Temp(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    sensorname = models.CharField(max_length=50)
    sensordata = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i40temp'
        unique_together = (('timestamp', 'sensorname'),)


class MiddleD004(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    ggq = models.TextField(db_column='GGQ', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(blank=True, null=True)
    ns = models.TextField(db_column='NS', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    ew = models.TextField(db_column='EW', blank=True, null=True)  # Field name made lowercase.
    gps = models.BigIntegerField(blank=True, null=True)
    sat = models.BigIntegerField(blank=True, null=True)
    qc = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    alt_ft = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'middle_d004'


class Resensys1HMedian(models.Model):
    timestamp = models.DateTimeField()
    sensorname = models.CharField(max_length=20)
    sensorvalue = models.FloatField()

    class Meta:
        managed = False
        db_table = 'resensys_1H_median'


class RoofD000(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    ggq = models.TextField(db_column='GGQ', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(blank=True, null=True)
    ns = models.TextField(db_column='NS', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    ew = models.TextField(db_column='EW', blank=True, null=True)  # Field name made lowercase.
    gps = models.BigIntegerField(blank=True, null=True)
    sat = models.BigIntegerField(blank=True, null=True)
    qc = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    alt_ft = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roof_d000'


class RoofD000Day(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    gps = models.BigIntegerField(blank=True, null=True)
    sat = models.FloatField(blank=True, null=True)
    qc = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    alt_ft = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roof_d000_day'


class Test(models.Model):
    pk_column = models.IntegerField(primary_key=True)
    column_1 = models.CharField(max_length=1)
    column_2 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


class Test2(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', blank=True, null=True)  # Field name made lowercase.
    test = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test2'


class Ultra(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    ne = models.FloatField(blank=True, null=True)
    se = models.FloatField(blank=True, null=True)
    nw = models.FloatField(blank=True, null=True)
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ultra'


class Users(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    sensorname = models.TextField(blank=True, null=True)
    sensordata = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UvaAtsRaw(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    pointname = models.CharField(max_length=50)
    northing = models.FloatField(blank=True, null=True)
    easting = models.FloatField(blank=True, null=True)
    elevation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uva_ats_raw'
        unique_together = (('timestamp', 'pointname'),)


class UvaAtsTemp(models.Model):
    timestamp = models.DateTimeField(primary_key=True)
    pointname = models.CharField(max_length=50)
    temp = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uva_ats_temp'
        unique_together = (('timestamp', 'pointname'),)


class UvaTiltRaw(models.Model):
    timestamp = models.DateTimeField(blank=True, null=True)
    sensorname = models.CharField(max_length=50, blank=True, null=True)
    sensordata = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uva_tilt_raw'


class WestD002(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    ggq = models.TextField(db_column='GGQ', blank=True, null=True)  # Field name made lowercase.
    long = models.FloatField(blank=True, null=True)
    ns = models.TextField(db_column='NS', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    ew = models.TextField(db_column='EW', blank=True, null=True)  # Field name made lowercase.
    gps = models.BigIntegerField(blank=True, null=True)
    sat = models.BigIntegerField(blank=True, null=True)
    qc = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    alt_ft = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'west_d002'


class WestD002Day(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    gps = models.BigIntegerField(blank=True, null=True)
    sat = models.FloatField(blank=True, null=True)
    qc = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    alt_ft = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'west_d002_day'
