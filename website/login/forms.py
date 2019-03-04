from django.contrib.auth.forms import UserCreationForm
from .models import DoctorUser
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)

class RegisterForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = DoctorUser
		fields = UserCreationForm.Meta.fields + ("email", )


class MyAuthenticationForm(AuthenticationForm):
#	class Meta(AuthenticationForm.Meta):
	pass


class MyPasswordChangeForm(PasswordChangeForm):
#	class Meta(PasswordChangeForm.Meta):
	pass


class MyPasswordResetForm(PasswordResetForm):
#	class Meta(PasswordResetForm.Meta):
	pass


class MySetPasswordForm(SetPasswordForm):
	#class Meta(SetPasswordForm.Meta):
	pass


