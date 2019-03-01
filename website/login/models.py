from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class DoctorUser(AbstractUser):
	email = models.EmailField(blank=True,unique=True,error_messages={'unique': ("Email already exists."),})
	class Meta(AbstractUser.Meta):
		pass


