# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tblfop(models.Model):
    record = models.IntegerField(db_column='RECORD', unique=True, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stan = models.CharField(db_column='STAN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activity_kinds = models.TextField(db_column='ACTIVITY_KINDS', blank=True, null=True)  # Field name made lowercase.
    registration = models.DateField(db_column='REGISTRATION', blank=True, null=True)  # Field name made lowercase.
    exchange_data = models.TextField(db_column='EXCHANGE_DATA', blank=True, null=True)  # Field name made lowercase.
    current_authority = models.CharField(db_column='CURRENT_AUTHORITY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    other_contact = models.CharField(db_column='OTHER_CONTACT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact_email = models.CharField(db_column='CONTACT_EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblFOP'


class Tbluo(models.Model):
    record = models.IntegerField(db_column='RECORD', unique=True, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=300, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opf = models.CharField(db_column='OPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    edrpou = models.IntegerField(db_column='EDRPOU', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stan = models.CharField(db_column='STAN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    activity_kinds = models.TextField(db_column='ACTIVITY_KINDS', blank=True, null=True)  # Field name made lowercase.
    registration = models.DateField(db_column='REGISTRATION', blank=True, null=True)  # Field name made lowercase.
    other_contact = models.CharField(db_column='OTHER_CONTACT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact_email = models.CharField(db_column='CONTACT_EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    exchange_data = models.TextField(db_column='EXCHANGE_DATA', blank=True, null=True)  # Field name made lowercase.
    founders = models.TextField(db_column='FOUNDERS', blank=True, null=True)  # Field name made lowercase.
    beneficiaries = models.TextField(db_column='BENEFICIARIES', blank=True, null=True)  # Field name made lowercase.
    signers = models.TextField(db_column='SIGNERS', blank=True, null=True)  # Field name made lowercase.
    authorized_capital = models.CharField(db_column='AUTHORIZED_CAPITAL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    statute = models.TextField(db_column='STATUTE', blank=True, null=True)  # Field name made lowercase.
    current_authority = models.TextField(db_column='CURRENT_AUTHORITY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblUO'
