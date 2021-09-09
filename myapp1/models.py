# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Consult(models.Model):
    consult_id = models.AutoField(db_column='consult_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField()
    patient = models.ForeignKey('Patients', models.DO_NOTHING, db_column='patient_ID')  # Field name made lowercase.
    doctor = models.ForeignKey('Doctors', models.DO_NOTHING)
    test = models.ForeignKey('Tests', models.DO_NOTHING, db_column='test_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consult'


class Doctors(models.Model):
    doctor_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'doctors'


class Patients(models.Model):
    patient_id = models.IntegerField(db_column='patient_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200)
    insurance = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    contactno = models.CharField(db_column='contactNo', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patients'


class Performed(models.Model):
    result_id = models.AutoField(db_column='result_ID', primary_key=True)  # Field name made lowercase.
    result = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'performed'


class Records(models.Model):
    record_id = models.AutoField(db_column='record_ID', primary_key=True)  # Field name made lowercase.
    test = models.ForeignKey('Tests', models.DO_NOTHING, db_column='test_ID')  # Field name made lowercase.
    doctor = models.ForeignKey(Doctors, models.DO_NOTHING)
    patient = models.ForeignKey(Patients, models.DO_NOTHING, db_column='patient_ID')  # Field name made lowercase.
    result = models.ForeignKey(Performed, models.DO_NOTHING, db_column='result_ID')  # Field name made lowercase.
    consult = models.ForeignKey(Consult, models.DO_NOTHING, db_column='consult_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'records'


class Tests(models.Model):
    test_id = models.IntegerField(primary_key=True)
    test_name = models.CharField(max_length=150)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tests'
