from django.contrib.auth.forms import UserCreationForm
from .models import DoctorUser

class RegisterForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = DoctorUser
		fields = UserCreationForm.Meta.fields + ("email", )
