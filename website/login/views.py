from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import DoctorUser
from .forms import RegisterForm,MyAuthenticationForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm#
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import views as auth_views#
from django.urls import reverse_lazy#




@login_required(login_url='/user/login')
def home(request):
	return render(request, 'home.html',{'username': request.user.username})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login:home'))
    else:
        form = RegisterForm()
    return  render(request, 'register.html', context={'form':form})




class MyLoginView(auth_views.LoginView):
	template_name='login.html'
	form_class = MyAuthenticationForm
#	class Meta(auth_views.LoginView.Meta):
#		pass



class MyLogoutView(auth_views.LogoutView):
#	class Meta(auth_views.LogoutView.Meta):
		pass



class MyPasswordChangeView(auth_views.PasswordChangeView):
	template_name='password_change_form.html'
	success_url = reverse_lazy('login:password_change_done')
	form_class = MyPasswordChangeForm
#	class Meta(auth_views.PasswordChangeView.Meta):
#		pass



class MyPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
	template_name='password_change_done.html'
#	class Meta(auth_views.PasswordChangeDoneView.Meta):
#		pass


class MyPasswordResetView(auth_views.PasswordResetView):
	template_name='password_reset_form.html'
	email_template_name = 'password_reset_email.html'
	success_url = reverse_lazy('login:password_reset_complete')
	form_class = MyPasswordResetForm
#	class Meta(auth_views.PasswordResetView.Meta):
#		pass



class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):
	template_name='password_reset_done.html'
#	class Meta(auth_views.PasswordResetDoneView.Meta):
#		pass



class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
	template_name='password_reset_confirm.html'
	success_url = reverse_lazy('login:password_reset_complete')
	form_class = MySetPasswordForm
#	class Meta(auth_views.PasswordResetCompleteView.Meta):
#		pass

class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
	template_name='password_reset_complete.html'




#def send(request):
#	if request.method == 'POST':
#		email = request.POST.get('email')
#		print(email)
#		msg='Forget password'
#		send_mail('Docy',msg,settings.EMAIL_FROM,[email])
#	return redirect(reverse('login:password_reset_done'))
