from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.mylogin, name='login'),
    path('register/',views.register, name='register'),
    path('change_password/',views.change_password, name='change_password'),
    path('logout/',views.mylogout, name='logout'),
]