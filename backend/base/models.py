from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True,blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(auto_now_add=True)
    createdAt =models.DateTimeField(auto_now_add=False, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2,null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postalCode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.address)

#-------------------------- CR1000 test ---------------------------

class Cr1000FtlaudMonitor(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    measure_avg = models.FloatField(db_column='measure_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp = models.FloatField(db_column='PTemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR1000_ftlaud_Monitor'
        unique_together = (('tmstamp', 'recnum'),)

#-------------------------- Mclean ----------------------------

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

#---------------------- NY17 ------------------------------------

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

#--------------Lulling -------------------------------
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
    sys2_temp_c_c1 = models.FloatField(db_column='Sys2_Temp_C_C2', blank=True, null=True)  # Field name made lowercase.

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

#----------------------------- DANZIGER ---------------------------------
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
