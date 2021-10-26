# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from datetime import datetime, date
from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import OrderBy


class Consult(models.Model):

    # Field name made lowercase.
    consult_id = models.AutoField(db_column='consult_ID', primary_key=True)
    date = models.DateField()
    # Field name made lowercase.
    patient = models.ForeignKey(
        'Patients', models.DO_NOTHING, db_column='patient_ID')
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING)
    # Field name made lowercase.
    test = models.ForeignKey('Tests', models.DO_NOTHING, db_column='test_ID')
    def __str__(self):
        date_to_string = str(self.date)
        format_datetime = datetime.strptime(date_to_string,"%Y-%m-%d")
        datetime_to_string = datetime.strftime(format_datetime, '%A, %b %d %y')
        return datetime_to_string

    class Meta:
        managed = True
        db_table = 'consult'


class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'doctors'


class Patients(models.Model):
    # Field name made lowercase.
    patient_id = models.AutoField(db_column='patient_ID', primary_key=True)
    name = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)
    # Field name made lowercase.
    contactno = models.CharField(db_column='contactNo', max_length=15)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

    class Meta:
        managed = True
        db_table = 'patients'


class Performed(models.Model):
    # Field name made lowercase.
    result_id = models.AutoField(db_column='result_ID', primary_key=True)
    result = models.CharField(max_length=20)

    def __str__(self):
        return self.result

    class Meta:
        managed = True
        db_table = 'performed'


class Records(models.Model):
    # Field name made lowercase.
    record_id = models.AutoField(db_column='record_ID', primary_key=True)
    # Field name made lowercase.
    test = models.ForeignKey('Tests', models.DO_NOTHING, db_column='test_ID')
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING)
    # Field name made lowercase.
    patient = models.ForeignKey(
        Patients, models.DO_NOTHING, db_column='patient_ID')
    # Field name made lowercase.
    result = models.ForeignKey(
        Performed, models.DO_NOTHING, db_column='result_ID')
    # Field name made lowercase.
    consult = models.ForeignKey(
        Consult, models.DO_NOTHING, db_column='consult_ID')

    class Meta:
        managed = True
        db_table = 'records'


class Tests(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=150)
    price = models.IntegerField()

    def __str__(self):
        return self.test_name

    class Meta:
        ordering = ('test_id',)
        managed = True
        db_table = 'tests'
