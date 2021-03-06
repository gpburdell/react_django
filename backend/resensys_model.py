#####################################

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    idaccount = models.AutoField(db_column='idAccount', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=45)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=45)  # Field name made lowercase.
    sidname = models.CharField(db_column='SIDName', max_length=45)  # Field name made lowercase.
    accounttype = models.CharField(db_column='AccountType', max_length=45)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LastLogin')  # Field name made lowercase.
    enable = models.IntegerField(db_column='Enable')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45)  # Field name made lowercase.
    email1 = models.CharField(db_column='Email1', max_length=45)  # Field name made lowercase.
    email2 = models.CharField(db_column='Email2', max_length=45)  # Field name made lowercase.
    email3 = models.CharField(db_column='Email3', max_length=45)  # Field name made lowercase.
    airupdateen = models.IntegerField(db_column='AirUpdateEn')  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate')  # Field name made lowercase.
    dongleincluded = models.IntegerField(db_column='DongleIncluded')  # Field name made lowercase.
    latitude = models.FloatField()
    longtitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Accounts'


class Activeusers(models.Model):
    idactiveusers = models.AutoField(db_column='idActiveUsers', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=45, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dbname = models.CharField(db_column='DBName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    alertactivated = models.IntegerField(db_column='AlertActivated', blank=True, null=True)  # Field name made lowercase.
    dbuid = models.CharField(db_column='DBUID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dbpsswd = models.CharField(db_column='DBPSSWD', max_length=45, blank=True, null=True)  # Field name made lowercase.
    usercreationtime = models.DateTimeField(db_column='UserCreationTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActiveUsers'


class Airupdate(models.Model):
    idairupdate = models.AutoField(db_column='idAirUpdate', primary_key=True)  # Field name made lowercase.
    siteid = models.PositiveIntegerField(db_column='SiteId', blank=True, null=True)  # Field name made lowercase.
    commandid = models.PositiveIntegerField(db_column='CommandId', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.PositiveIntegerField(db_column='DeviceId', blank=True, null=True)  # Field name made lowercase.
    value = models.PositiveIntegerField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    firmwareversion = models.PositiveIntegerField(db_column='FirmwareVersion', blank=True, null=True)  # Field name made lowercase.
    reserve = models.PositiveIntegerField(db_column='Reserve', blank=True, null=True)  # Field name made lowercase.
    status = models.PositiveIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    insertiontime = models.DateTimeField(db_column='InsertionTime', blank=True, null=True)  # Field name made lowercase.
    executiontime = models.DateTimeField(db_column='ExecutionTime', blank=True, null=True)  # Field name made lowercase.
    seqnum = models.PositiveIntegerField(db_column='SeqNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AirUpdate'


class Alert(models.Model):
    idalert = models.AutoField(db_column='idAlert', primary_key=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceID', blank=True, null=True)  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    alerttype = models.IntegerField(db_column='AlertType', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    interval = models.CharField(db_column='Interval', max_length=45, blank=True, null=True)  # Field name made lowercase.
    offset = models.FloatField(db_column='Offset', blank=True, null=True)  # Field name made lowercase.
    coef = models.FloatField(db_column='Coef', blank=True, null=True)  # Field name made lowercase.
    tempoffset = models.FloatField(db_column='TempOffset', blank=True, null=True)  # Field name made lowercase.
    tempcoef = models.FloatField(db_column='TempCoef', blank=True, null=True)  # Field name made lowercase.
    deviceid2 = models.IntegerField(db_column='DeviceID2', blank=True, null=True)  # Field name made lowercase.
    siteid2 = models.IntegerField(db_column='SiteID2', blank=True, null=True)  # Field name made lowercase.
    quantity2 = models.IntegerField(db_column='Quantity2', blank=True, null=True)  # Field name made lowercase.
    offset2 = models.FloatField(db_column='Offset2', blank=True, null=True)  # Field name made lowercase.
    coef2 = models.FloatField(db_column='Coef2', blank=True, null=True)  # Field name made lowercase.
    tempoffset2 = models.FloatField(db_column='TempOffset2', blank=True, null=True)  # Field name made lowercase.
    tempcoef2 = models.FloatField(db_column='TempCoef2', blank=True, null=True)  # Field name made lowercase.
    lowlow = models.FloatField(db_column='LowLow', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    highhigh = models.FloatField(db_column='HighHigh', blank=True, null=True)  # Field name made lowercase.
    activated = models.IntegerField(db_column='Activated', blank=True, null=True)  # Field name made lowercase.
    lastupdatedatetime = models.DateTimeField(db_column='LastUpdateDateTime', blank=True, null=True)  # Field name made lowercase.
    lastupdateby = models.CharField(db_column='LastUpdateBy', max_length=45, blank=True, null=True)  # Field name made lowercase.
    laststatuschangedatetime = models.DateTimeField(db_column='LastStatusChangeDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alert'


class Alert2D(models.Model):
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    did1 = models.CharField(db_column='DID1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dname1 = models.CharField(db_column='DNAME1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sid1 = models.CharField(db_column='SID1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sname1 = models.CharField(db_column='SNAME1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dataformat1 = models.IntegerField(db_column='DATAFORMAT1', blank=True, null=True)  # Field name made lowercase.
    quantityname1 = models.CharField(db_column='QUANTITYNAME1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    coef1 = models.FloatField(db_column='COEF1', blank=True, null=True)  # Field name made lowercase.
    doff1 = models.FloatField(db_column='DOFF1', blank=True, null=True)  # Field name made lowercase.
    tempcoef1 = models.FloatField(db_column='TEMPCOEF1', blank=True, null=True)  # Field name made lowercase.
    did2 = models.CharField(db_column='DID2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dname2 = models.CharField(db_column='DNAME2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sid2 = models.CharField(db_column='SID2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sname2 = models.CharField(db_column='SNAME2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dataformat2 = models.IntegerField(db_column='DATAFORMAT2', blank=True, null=True)  # Field name made lowercase.
    quantityname2 = models.CharField(db_column='QUANTITYNAME2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    coef2 = models.FloatField(db_column='COEF2', blank=True, null=True)  # Field name made lowercase.
    doff2 = models.FloatField(db_column='DOFF2', blank=True, null=True)  # Field name made lowercase.
    tempcoef2 = models.FloatField(db_column='TEMPCOEF2', blank=True, null=True)  # Field name made lowercase.
    w1x = models.FloatField(db_column='W1X', blank=True, null=True)  # Field name made lowercase.
    w1y = models.FloatField(db_column='W1Y', blank=True, null=True)  # Field name made lowercase.
    w2x = models.FloatField(db_column='W2X', blank=True, null=True)  # Field name made lowercase.
    w2y = models.FloatField(db_column='W2Y', blank=True, null=True)  # Field name made lowercase.
    w3x = models.FloatField(db_column='W3X', blank=True, null=True)  # Field name made lowercase.
    w3y = models.FloatField(db_column='W3Y', blank=True, null=True)  # Field name made lowercase.
    w4x = models.FloatField(db_column='W4X', blank=True, null=True)  # Field name made lowercase.
    w4y = models.FloatField(db_column='W4Y', blank=True, null=True)  # Field name made lowercase.
    a1x = models.FloatField(db_column='A1X', blank=True, null=True)  # Field name made lowercase.
    a1y = models.FloatField(db_column='A1Y', blank=True, null=True)  # Field name made lowercase.
    a2x = models.FloatField(db_column='A2X', blank=True, null=True)  # Field name made lowercase.
    a2y = models.FloatField(db_column='A2Y', blank=True, null=True)  # Field name made lowercase.
    a3x = models.FloatField(db_column='A3X', blank=True, null=True)  # Field name made lowercase.
    a3y = models.FloatField(db_column='A3Y', blank=True, null=True)  # Field name made lowercase.
    a4x = models.FloatField(db_column='A4X', blank=True, null=True)  # Field name made lowercase.
    a4y = models.FloatField(db_column='A4Y', blank=True, null=True)  # Field name made lowercase.
    alertinterval = models.CharField(db_column='AlertInterval', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email1 = models.CharField(db_column='Email1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='Email2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email3 = models.CharField(db_column='Email3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    activated = models.IntegerField(db_column='Activated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Alert2D'


class Alertemails(models.Model):
    idalertemails = models.AutoField(db_column='idAlertEmails', primary_key=True)  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertEmails'


class Alertgen(models.Model):
    idalertgen = models.AutoField(db_column='idAlertGen', primary_key=True)  # Field name made lowercase.
    alerttype = models.IntegerField(db_column='AlertType', blank=True, null=True)  # Field name made lowercase.
    alertstatus = models.IntegerField(db_column='AlertStatus', blank=True, null=True)  # Field name made lowercase.
    alertinterval = models.CharField(db_column='AlertInterval', max_length=45, blank=True, null=True)  # Field name made lowercase.
    deviceid1 = models.CharField(db_column='DeviceID1', max_length=18, blank=True, null=True)  # Field name made lowercase.
    siteid1 = models.CharField(db_column='SiteID1', max_length=18, blank=True, null=True)  # Field name made lowercase.
    quantity1 = models.IntegerField(db_column='Quantity1', blank=True, null=True)  # Field name made lowercase.
    offset1 = models.FloatField(db_column='Offset1', blank=True, null=True)  # Field name made lowercase.
    coef1 = models.FloatField(db_column='Coef1', blank=True, null=True)  # Field name made lowercase.
    tempoffset1 = models.FloatField(db_column='TempOffset1', blank=True, null=True)  # Field name made lowercase.
    tempcoef1 = models.FloatField(db_column='TempCoef1', blank=True, null=True)  # Field name made lowercase.
    deviceid2 = models.CharField(db_column='DeviceID2', max_length=18, blank=True, null=True)  # Field name made lowercase.
    siteid2 = models.CharField(db_column='SiteID2', max_length=18, blank=True, null=True)  # Field name made lowercase.
    quantity2 = models.IntegerField(db_column='Quantity2', blank=True, null=True)  # Field name made lowercase.
    offset2 = models.FloatField(db_column='Offset2', blank=True, null=True)  # Field name made lowercase.
    coef2 = models.FloatField(db_column='Coef2', blank=True, null=True)  # Field name made lowercase.
    tempoffset2 = models.FloatField(db_column='TempOffset2', blank=True, null=True)  # Field name made lowercase.
    tempcoef2 = models.FloatField(db_column='TempCoef2', blank=True, null=True)  # Field name made lowercase.
    warning_ll_1 = models.FloatField(db_column='WARNING_LL_1', blank=True, null=True)  # Field name made lowercase.
    warning_ll_2 = models.FloatField(db_column='WARNING_LL_2', blank=True, null=True)  # Field name made lowercase.
    warning_hl_1 = models.FloatField(db_column='WARNING_HL_1', blank=True, null=True)  # Field name made lowercase.
    warning_hl_2 = models.FloatField(db_column='WARNING_HL_2', blank=True, null=True)  # Field name made lowercase.
    warning_hh_1 = models.FloatField(db_column='WARNING_HH_1', blank=True, null=True)  # Field name made lowercase.
    warning_hh_2 = models.FloatField(db_column='WARNING_HH_2', blank=True, null=True)  # Field name made lowercase.
    warning_lh_1 = models.FloatField(db_column='WARNING_LH_1', blank=True, null=True)  # Field name made lowercase.
    warning_lh_2 = models.FloatField(db_column='WARNING_LH_2', blank=True, null=True)  # Field name made lowercase.
    alarm_ll_1 = models.FloatField(db_column='ALARM_LL_1', blank=True, null=True)  # Field name made lowercase.
    alarm_ll_2 = models.FloatField(db_column='ALARM_LL_2', blank=True, null=True)  # Field name made lowercase.
    alarm_hl_1 = models.FloatField(db_column='ALARM_HL_1', blank=True, null=True)  # Field name made lowercase.
    alarm_hl_2 = models.FloatField(db_column='ALARM_HL_2', blank=True, null=True)  # Field name made lowercase.
    alarm_hh_1 = models.FloatField(db_column='ALARM_HH_1', blank=True, null=True)  # Field name made lowercase.
    alarm_hh_2 = models.FloatField(db_column='ALARM_HH_2', blank=True, null=True)  # Field name made lowercase.
    alarm_lh_1 = models.FloatField(db_column='ALARM_LH_1', blank=True, null=True)  # Field name made lowercase.
    alarm_lh_2 = models.FloatField(db_column='ALARM_LH_2', blank=True, null=True)  # Field name made lowercase.
    activated = models.IntegerField(db_column='Activated', blank=True, null=True)  # Field name made lowercase.
    lastmodifdatetime = models.DateTimeField(db_column='LastModifDateTime', blank=True, null=True)  # Field name made lowercase.
    lastmodifby = models.CharField(db_column='LastModifBy', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email1 = models.CharField(db_column='Email1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email2 = models.CharField(db_column='Email2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email3 = models.CharField(db_column='Email3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email4 = models.CharField(db_column='Email4', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email5 = models.CharField(db_column='Email5', max_length=45, blank=True, null=True)  # Field name made lowercase.
    timeframe = models.IntegerField(db_column='TimeFrame', blank=True, null=True)  # Field name made lowercase.
    synchronizationmethod = models.IntegerField(db_column='SynchronizationMethod', blank=True, null=True)  # Field name made lowercase.
    quantity1name = models.CharField(db_column='Quantity1Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantity2name = models.CharField(db_column='Quantity2name', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertGen'
        unique_together = (('deviceid1', 'siteid1', 'quantity1'),)


class Alertparam(models.Model):
    idalert = models.AutoField(db_column='idAlert', primary_key=True)  # Field name made lowercase.
    alerttype = models.IntegerField(db_column='AlertType')  # Field name made lowercase.
    associationset = models.CharField(db_column='AssociationSet', max_length=500)  # Field name made lowercase.
    dataformatset = models.CharField(db_column='DataFormatSet', max_length=500)  # Field name made lowercase.
    lastupdate = models.DateTimeField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    interupdatetime = models.IntegerField(db_column='InterUpdateTime')  # Field name made lowercase.
    param1 = models.FloatField(db_column='Param1')  # Field name made lowercase.
    param2 = models.FloatField(db_column='Param2')  # Field name made lowercase.
    param3 = models.FloatField(db_column='Param3')  # Field name made lowercase.
    param4 = models.FloatField(db_column='Param4')  # Field name made lowercase.
    param5 = models.FloatField(db_column='Param5')  # Field name made lowercase.
    ack = models.IntegerField(db_column='Ack')  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    colorcode = models.IntegerField(db_column='ColorCode')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=500)  # Field name made lowercase.
    siteidset = models.CharField(db_column='SiteIDSet', max_length=500)  # Field name made lowercase.
    idalerthist = models.CharField(db_column='idAlertHist', max_length=500, blank=True, null=True)  # Field name made lowercase.
    indpndntassocset = models.CharField(db_column='IndpndntAssocSet', max_length=500)  # Field name made lowercase.
    inpndntdataformatset = models.CharField(db_column='InpndntDataFormatSet', max_length=500)  # Field name made lowercase.
    indpndntsiteidset = models.CharField(db_column='IndpndntSiteIDSet', max_length=500)  # Field name made lowercase.
    cutoffratiofilter = models.FloatField(db_column='CutOffRatioFilter')  # Field name made lowercase.
    filterorder = models.SmallIntegerField(db_column='FilterOrder')  # Field name made lowercase.
    numberofsubintervals = models.IntegerField(db_column='NumberOfSubIntervals')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertParam'


class Alertstatus(models.Model):
    idalertstatus = models.AutoField(db_column='idAlertStatus', primary_key=True)  # Field name made lowercase.
    idalert = models.IntegerField(db_column='idAlert', blank=True, null=True)  # Field name made lowercase.
    deviceid = models.CharField(db_column='DeviceID', max_length=12, blank=True, null=True)  # Field name made lowercase.
    quantity = models.CharField(db_column='Quantity', max_length=8, blank=True, null=True)  # Field name made lowercase.
    siteid = models.CharField(db_column='SiteID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.
    alerttype = models.CharField(db_column='AlertType', max_length=2, blank=True, null=True)  # Field name made lowercase.
    lastupdatetime = models.DateTimeField(db_column='LastUpdateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlertStatus'


class Info(models.Model):
    idinfo = models.AutoField(db_column='idInfo', primary_key=True)  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    ttl = models.CharField(db_column='TTL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ = models.CharField(db_column='TYP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pfil = models.CharField(db_column='PFil', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stt = models.IntegerField(db_column='STT', blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    firmver = models.IntegerField(db_column='FirmVer')  # Field name made lowercase.
    m1 = models.IntegerField(db_column='M1', blank=True, null=True)  # Field name made lowercase.
    dof1 = models.FloatField(db_column='DOF1', blank=True, null=True)  # Field name made lowercase.
    cof1 = models.FloatField(db_column='COF1', blank=True, null=True)  # Field name made lowercase.
    m2 = models.IntegerField(db_column='M2', blank=True, null=True)  # Field name made lowercase.
    dof2 = models.FloatField(db_column='DOF2', blank=True, null=True)  # Field name made lowercase.
    cof2 = models.FloatField(db_column='COF2', blank=True, null=True)  # Field name made lowercase.
    m3 = models.IntegerField(db_column='M3', blank=True, null=True)  # Field name made lowercase.
    dof3 = models.FloatField(db_column='DOF3', blank=True, null=True)  # Field name made lowercase.
    cof3 = models.FloatField(db_column='COF3', blank=True, null=True)  # Field name made lowercase.
    m4 = models.IntegerField(db_column='M4', blank=True, null=True)  # Field name made lowercase.
    dof4 = models.FloatField(db_column='DOF4', blank=True, null=True)  # Field name made lowercase.
    cof4 = models.FloatField(db_column='COF4', blank=True, null=True)  # Field name made lowercase.
    m5 = models.IntegerField(db_column='M5')  # Field name made lowercase.
    dof5 = models.FloatField(db_column='DOF5')  # Field name made lowercase.
    cof5 = models.FloatField(db_column='COF5')  # Field name made lowercase.
    m6 = models.IntegerField(db_column='M6')  # Field name made lowercase.
    dof6 = models.FloatField(db_column='DOF6')  # Field name made lowercase.
    cof6 = models.FloatField(db_column='COF6')  # Field name made lowercase.
    m7 = models.IntegerField(db_column='M7')  # Field name made lowercase.
    dof7 = models.FloatField(db_column='DOF7')  # Field name made lowercase.
    cof7 = models.FloatField(db_column='COF7')  # Field name made lowercase.
    m8 = models.IntegerField(db_column='M8')  # Field name made lowercase.
    dof8 = models.FloatField(db_column='DOF8')  # Field name made lowercase.
    cof8 = models.FloatField(db_column='COF8')  # Field name made lowercase.
    m9 = models.IntegerField(db_column='M9')  # Field name made lowercase.
    dof9 = models.FloatField(db_column='DOF9')  # Field name made lowercase.
    cof9 = models.FloatField(db_column='COF9')  # Field name made lowercase.
    m10 = models.IntegerField(db_column='M10')  # Field name made lowercase.
    dof10 = models.FloatField(db_column='DOF10')  # Field name made lowercase.
    cof10 = models.FloatField(db_column='COF10')  # Field name made lowercase.
    last_changed_by = models.CharField(db_column='Last_Changed_By', max_length=45, blank=True, null=True)  # Field name made lowercase.
    last_update = models.DateTimeField(db_column='Last_Update', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Info'


class InfoHist(models.Model):
    idinfo = models.AutoField(db_column='idInfo', primary_key=True)  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    ttl = models.CharField(db_column='TTL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='DES', max_length=50, blank=True, null=True)  # Field name made lowercase.
    typ = models.CharField(db_column='TYP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pfil = models.CharField(db_column='PFil', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stt = models.IntegerField(db_column='STT', blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=11, blank=True, null=True)  # Field name made lowercase.
    firmver = models.IntegerField(db_column='FirmVer')  # Field name made lowercase.
    m1 = models.IntegerField(db_column='M1', blank=True, null=True)  # Field name made lowercase.
    dof1 = models.FloatField(db_column='DOF1', blank=True, null=True)  # Field name made lowercase.
    cof1 = models.FloatField(db_column='COF1', blank=True, null=True)  # Field name made lowercase.
    m2 = models.IntegerField(db_column='M2', blank=True, null=True)  # Field name made lowercase.
    dof2 = models.FloatField(db_column='DOF2', blank=True, null=True)  # Field name made lowercase.
    cof2 = models.FloatField(db_column='COF2', blank=True, null=True)  # Field name made lowercase.
    m3 = models.IntegerField(db_column='M3', blank=True, null=True)  # Field name made lowercase.
    dof3 = models.FloatField(db_column='DOF3', blank=True, null=True)  # Field name made lowercase.
    cof3 = models.FloatField(db_column='COF3', blank=True, null=True)  # Field name made lowercase.
    m4 = models.IntegerField(db_column='M4', blank=True, null=True)  # Field name made lowercase.
    dof4 = models.FloatField(db_column='DOF4', blank=True, null=True)  # Field name made lowercase.
    cof4 = models.FloatField(db_column='COF4', blank=True, null=True)  # Field name made lowercase.
    m5 = models.IntegerField(db_column='M5')  # Field name made lowercase.
    dof5 = models.FloatField(db_column='DOF5')  # Field name made lowercase.
    cof5 = models.FloatField(db_column='COF5')  # Field name made lowercase.
    m6 = models.IntegerField(db_column='M6')  # Field name made lowercase.
    dof6 = models.FloatField(db_column='DOF6')  # Field name made lowercase.
    cof6 = models.FloatField(db_column='COF6')  # Field name made lowercase.
    m7 = models.IntegerField(db_column='M7')  # Field name made lowercase.
    dof7 = models.FloatField(db_column='DOF7')  # Field name made lowercase.
    cof7 = models.FloatField(db_column='COF7')  # Field name made lowercase.
    m8 = models.IntegerField(db_column='M8')  # Field name made lowercase.
    dof8 = models.FloatField(db_column='DOF8')  # Field name made lowercase.
    cof8 = models.FloatField(db_column='COF8')  # Field name made lowercase.
    m9 = models.IntegerField(db_column='M9')  # Field name made lowercase.
    dof9 = models.FloatField(db_column='DOF9')  # Field name made lowercase.
    cof9 = models.FloatField(db_column='COF9')  # Field name made lowercase.
    m10 = models.IntegerField(db_column='M10')  # Field name made lowercase.
    dof10 = models.FloatField(db_column='DOF10')  # Field name made lowercase.
    cof10 = models.FloatField(db_column='COF10')  # Field name made lowercase.
    last_changed_by = models.CharField(db_column='Last_Changed_By', max_length=45, blank=True, null=True)  # Field name made lowercase.
    last_update = models.DateTimeField(db_column='Last_Update', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Info_Hist'


class Quantityinfo(models.Model):
    dataformat = models.IntegerField(db_column='DataFormat', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=45, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=45, blank=True, null=True)  # Field name made lowercase.
    picture = models.CharField(db_column='Picture', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precision = models.CharField(db_column='Precision', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numprecision = models.IntegerField(db_column='NumPrecision', blank=True, null=True)  # Field name made lowercase.
    calibcoef = models.FloatField(db_column='CalibCoef', blank=True, null=True)  # Field name made lowercase.
    caliboffset = models.FloatField(db_column='CalibOffset', blank=True, null=True)  # Field name made lowercase.
    defaultmax = models.FloatField(db_column='DefaultMax', blank=True, null=True)  # Field name made lowercase.
    defaultmin = models.FloatField(db_column='DefaultMin', blank=True, null=True)  # Field name made lowercase.
    synctype = models.CharField(db_column='SyncType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    showable = models.CharField(db_column='Showable', max_length=45, blank=True, null=True)  # Field name made lowercase.
    triggertresholddefault = models.FloatField(db_column='TriggerTresholdDefault', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperioddefault = models.FloatField(db_column='TriggerSamplingPeriodDefault', blank=True, null=True)  # Field name made lowercase.
    triggertresholdmax = models.FloatField(db_column='TriggerTresholdMax', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperiodmax = models.FloatField(db_column='TriggerSamplingPeriodMax', blank=True, null=True)  # Field name made lowercase.
    triggertresholdmin = models.FloatField(db_column='TriggerTresholdMin', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperiodmin = models.FloatField(db_column='TriggerSamplingPeriodMin', blank=True, null=True)  # Field name made lowercase.
    triggertresholdstep = models.FloatField(db_column='TriggerTresholdStep', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperiodstep = models.FloatField(db_column='TriggerSamplingPeriodStep', blank=True, null=True)  # Field name made lowercase.
    datetimeformat = models.CharField(db_column='DateTimeFormat', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityInfo'


class Quantityinfo2(models.Model):
    dataformat = models.IntegerField(db_column='DataFormat', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(db_column='Version', max_length=45, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=45, blank=True, null=True)  # Field name made lowercase.
    picture = models.CharField(db_column='Picture', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    precision = models.CharField(db_column='Precision', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numprecision = models.IntegerField(db_column='NumPrecision', blank=True, null=True)  # Field name made lowercase.
    calibcoef = models.FloatField(db_column='CalibCoef', blank=True, null=True)  # Field name made lowercase.
    caliboffset = models.FloatField(db_column='CalibOffset', blank=True, null=True)  # Field name made lowercase.
    defaultmax = models.FloatField(db_column='DefaultMax', blank=True, null=True)  # Field name made lowercase.
    defaultmin = models.FloatField(db_column='DefaultMin', blank=True, null=True)  # Field name made lowercase.
    synctype = models.CharField(db_column='SyncType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    showable = models.CharField(db_column='Showable', max_length=45, blank=True, null=True)  # Field name made lowercase.
    triggertresholddefault = models.FloatField(db_column='TriggerTresholdDefault', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperioddefault = models.FloatField(db_column='TriggerSamplingPeriodDefault', blank=True, null=True)  # Field name made lowercase.
    triggertresholdmax = models.FloatField(db_column='TriggerTresholdMax', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperiodmax = models.FloatField(db_column='TriggerSamplingPeriodMax', blank=True, null=True)  # Field name made lowercase.
    triggertresholdmin = models.FloatField(db_column='TriggerTresholdMin', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperiodmin = models.FloatField(db_column='TriggerSamplingPeriodMin', blank=True, null=True)  # Field name made lowercase.
    triggertresholdstep = models.FloatField(db_column='TriggerTresholdStep', blank=True, null=True)  # Field name made lowercase.
    triggersamplingperiodstep = models.FloatField(db_column='TriggerSamplingPeriodStep', blank=True, null=True)  # Field name made lowercase.
    datetimeformat = models.CharField(db_column='DateTimeFormat', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityInfo2'


class Quantitylist(models.Model):
    idquantity = models.AutoField(db_column='idQuantity', primary_key=True)  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=120, blank=True, null=True)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SNAME', max_length=120, blank=True, null=True)  # Field name made lowercase.
    dtype = models.CharField(db_column='DTYPE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dataformat = models.CharField(db_column='DATAFORMAT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    quantityname = models.CharField(db_column='QUANTITYNAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='UNIT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numberformat = models.CharField(db_column='NUMBERFORMAT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numprecision = models.IntegerField(db_column='NUMPRECISION', blank=True, null=True)  # Field name made lowercase.
    calibcoef = models.FloatField(db_column='CALIBCOEF', blank=True, null=True)  # Field name made lowercase.
    calibdoff = models.FloatField(db_column='CALIBDOFF', blank=True, null=True)  # Field name made lowercase.
    calibtempcoef = models.FloatField(db_column='CALIBTEMPCOEF', blank=True, null=True)  # Field name made lowercase.
    samplinginterval = models.IntegerField(db_column='SAMPLINGINTERVAL', blank=True, null=True)  # Field name made lowercase.
    thrll = models.FloatField(db_column='THRLL', blank=True, null=True)  # Field name made lowercase.
    thrl = models.FloatField(db_column='THRL', blank=True, null=True)  # Field name made lowercase.
    thrh = models.FloatField(db_column='THRH', blank=True, null=True)  # Field name made lowercase.
    thrhh = models.FloatField(db_column='THRHH', blank=True, null=True)  # Field name made lowercase.
    datetimeformat = models.CharField(db_column='DATETIMEFORMAT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    showthr = models.IntegerField(db_column='SHOWTHR', blank=True, null=True)  # Field name made lowercase.
    applyoptionaloffset = models.IntegerField(db_column='APPLYOPTIONALOFFSET', blank=True, null=True)  # Field name made lowercase.
    eventdetthr = models.FloatField(db_column='EVENTDETTHR', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'QuantityList'
        unique_together = (('did', 'sid', 'dataformat'),)


class Status(models.Model):
    idstatus = models.AutoField(db_column='idStatus', primary_key=True)  # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceID', blank=True, null=True)  # Field name made lowercase.
    siteid = models.IntegerField(db_column='SiteID', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    alerttype = models.IntegerField(db_column='AlertType', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    interval = models.CharField(db_column='Interval', max_length=45, blank=True, null=True)  # Field name made lowercase.
    offset = models.FloatField(db_column='Offset', blank=True, null=True)  # Field name made lowercase.
    coef = models.FloatField(db_column='Coef', blank=True, null=True)  # Field name made lowercase.
    tempoffset = models.FloatField(db_column='TempOffset', blank=True, null=True)  # Field name made lowercase.
    tempcoef = models.FloatField(db_column='TempCoef', blank=True, null=True)  # Field name made lowercase.
    deviceid2 = models.IntegerField(db_column='DeviceID2', blank=True, null=True)  # Field name made lowercase.
    siteid2 = models.IntegerField(db_column='SiteID2', blank=True, null=True)  # Field name made lowercase.
    quantity2 = models.IntegerField(db_column='Quantity2', blank=True, null=True)  # Field name made lowercase.
    offset2 = models.FloatField(db_column='Offset2', blank=True, null=True)  # Field name made lowercase.
    coef2 = models.FloatField(db_column='Coef2', blank=True, null=True)  # Field name made lowercase.
    tempoffset2 = models.FloatField(db_column='TempOffset2', blank=True, null=True)  # Field name made lowercase.
    tempcoef2 = models.FloatField(db_column='TempCoef2', blank=True, null=True)  # Field name made lowercase.
    lowlow = models.FloatField(db_column='LowLow', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='Low', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    highhigh = models.FloatField(db_column='HighHigh', blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.
    lastupdatedatetime = models.DateTimeField(db_column='LastUpdateDateTime', blank=True, null=True)  # Field name made lowercase.
    max = models.FloatField(db_column='Max', blank=True, null=True)  # Field name made lowercase.
    min = models.FloatField(db_column='Min', blank=True, null=True)  # Field name made lowercase.
    average = models.FloatField(db_column='Average', blank=True, null=True)  # Field name made lowercase.
    llcount = models.IntegerField(db_column='LLCount', blank=True, null=True)  # Field name made lowercase.
    lcount = models.IntegerField(db_column='LCount', blank=True, null=True)  # Field name made lowercase.
    hcount = models.IntegerField(db_column='HCount', blank=True, null=True)  # Field name made lowercase.
    hhcount = models.IntegerField(db_column='HHCount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Status'


class Tempcalib(models.Model):
    idtempcalib = models.AutoField(db_column='idTempCalib', primary_key=True)  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length=11)  # Field name made lowercase.
    sid = models.CharField(db_column='SID', max_length=11)  # Field name made lowercase.
    dataformat = models.IntegerField(db_column='DataFormat')  # Field name made lowercase.
    dof = models.FloatField(db_column='DOF')  # Field name made lowercase.
    cof = models.FloatField(db_column='COF')  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time')  # Field name made lowercase.
    calibstarttime = models.DateTimeField(db_column='CalibStartTime')  # Field name made lowercase.
    calibendtime = models.DateTimeField(db_column='CalibEndTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TempCalib'
