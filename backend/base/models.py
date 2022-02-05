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

class Cr1000FtlaudMonitor(models.Model):
    tmstamp = models.DateTimeField(db_column='TmStamp', primary_key=True)  # Field name made lowercase.
    recnum = models.BigIntegerField(db_column='RecNum')  # Field name made lowercase.
    measure_avg = models.FloatField(db_column='measure_Avg', blank=True, null=True)  # Field name made lowercase.
    ptemp = models.FloatField(db_column='PTemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CR1000_ftlaud_Monitor'
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