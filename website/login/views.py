from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import DoctorUser
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings

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


#def send(request):
#	if request.method == 'POST':
#		email = request.POST.get('email')
#		print(email)
#		msg='Forget password'
#		send_mail('Docy',msg,settings.EMAIL_FROM,[email])
#	return redirect(reverse('login:password_reset_done'))
