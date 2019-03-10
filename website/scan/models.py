from django.db import models
from django.conf import settings
from django.forms import ModelForm
from django import forms
import os
import uuid

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        )
    pid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(null=True,blank=True)
    Chemo = models.BooleanField(null=True,blank=True)
    Last_Chemo = models.DateField(null=True,blank=True)
    smoker = models.BooleanField(null=True,blank=True)
    Packs_yearly = models.FloatField(null=True,blank=True)
    diabetes = models.BooleanField(null=True,blank=True)
    insulin = models.BooleanField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)

    def delete(self, *args, **kwargs):
        # override delete method to delete all scan files of the patient
        scans = self.scan_set.all()
        for scan in scans:
            scan.delete()
        super().delete(*args, **kwargs)

    def toView(self):
        # Converts to frontend view representation

        return {
            'pid': self.pid,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birth_date': self.birth_date,
            'gender': self.gender,
            'age': self.age,
            'Chemo': self.Chemo,
            'Last_Chemo': self.Last_Chemo,
            'smoker': self.smoker,
            'Packs_yearly': self.Packs_yearly,
            'diabetes': self.diabetes,
            'insulin': self.insulin,
            'weight': self.weight,
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(),
            'Last_Chemo': DateInput()
        }

def user_directory_path(instance, filename):
    # random file name
    ext = filename.split('.')[-1]
    filename = str(uuid.uuid4().hex) + '.' + ext
    return filename

class Scan(models.Model):
    sid = models.AutoField(primary_key=True)

   # doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    diag_date = models.DateField(null=True,blank=True)
    diagnosis = models.CharField(max_length=200)
    reason = models.CharField(max_length=200,blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=user_directory_path)

    def delete(self, *args, **kwargs):
        # override delete method to delete the file
        self.file.delete()
        super().delete(*args, **kwargs)

    def toView(self):
        # Converts to frontend view representation

        return {
            'sid': self.sid,
            'diag_date': self.diag_date,
            'diagnosis': self.diagnosis,
            'reason': self.reason,
           # 'doctor': AUTH_USER_MODEL.first_name+ AUTH_USER_MODEL.last_name
           
        }

class ScanForm(ModelForm):
    class Meta:
        model = Scan
        fields = ['sid','diag_date','diagnosis','reason', 'file']
        widgets = {
            'diag_date': DateInput()
        }
