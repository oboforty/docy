from django.db import models
from django.conf import settings
import uuid
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        )
    pid = models.AutoField(primary_key=True)
    name_validator = RegexValidator(regex=r'^[a-zA-Z ]+$', message='Only letters and spaces are allowed.')
    first_name = models.CharField(max_length=20, validators=[name_validator])
    last_name = models.CharField(max_length=20, validators=[name_validator])
    birth_date = models.DateField(validators=[MinValueValidator(datetime.date(1900, 1, 1)), MaxValueValidator(datetime.date.today())])
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    Chemo = models.BooleanField(null=True,blank=True)
    Last_Chemo = models.DateField(null=True,blank=True)
    smoker = models.BooleanField(null=True,blank=True)
    Packs_yearly = models.FloatField(null=True,blank=True)
    diabetes = models.BooleanField(null=True,blank=True)
    insulin = models.BooleanField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True, validators=[MinValueValidator(0), MaxValueValidator(500)])

    def delete(self, *args, **kwargs):
        # override delete method to delete all scan files of the patient
        scans = self.scan_set.all()
        for scan in scans:
            scan.delete()
        super().delete(*args, **kwargs)
    
    def age(self):
        return datetime.date.today().year - self.birth_date.year

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


def user_directory_path(instance, filename):
    # random file name
    ext = filename.split('.')[-1]
    filename = str(uuid.uuid4().hex) + '.' + ext
    return filename

def validate_size(value):
    # validate the size of upload image <= 200MB
    max_size = 2 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError('Image size should not exceed 2 MB!')

class Scan(models.Model):
    sid = models.AutoField(primary_key=True)

    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    diag_date = models.DateField(default=datetime.date.today())
    diagnosis = models.CharField(max_length=200)
    reason = models.CharField(max_length=200,blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    scan = models.ImageField(upload_to=user_directory_path, validators=[validate_size])

    def delete(self, *args, **kwargs):
        # override delete method to delete the file
        self.scan.delete()
        super().delete(*args, **kwargs)

    def toView(self):
        # Converts to frontend view representation

        return {
            'sid': self.sid,
            'diag_date': self.diag_date,
            'diagnosis': self.diagnosis,
            'reason': self.reason,
            'doctor': AUTH_USER_MODEL.first_name+ AUTH_USER_MODEL.last_name
           
        }
