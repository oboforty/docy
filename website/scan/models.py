from django.db import models
from django.conf import settings
#not sure if this user can be used for foreignkey


# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES=(
        (1,'Male'),
        (2,'Female'),
        )
    pid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField()
    Chemo = models.BooleanField()
    Last_Chemo = models.DateField()
    smoker = models.BooleanField()
    Packs_yearly = models.IntegerField()
    diabetes = models.BooleanField()
    insulin = models.BooleanField()
    weight = models.FloatField()

class Scan(models.Model):
    sid = models.AutoField(primary_key=True)
    pid = models.ForeignKey('Patient',on_delete=models.CASCADE)
    dia_id = models.ForeignKey('Diagnosis',on_delete=models.CASCADE)

    doctor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Diagnosis(models.Model):
    dia_id = models.AutoField(primary_key=True)
    diagnosis = models.CharField(max_length=20)
