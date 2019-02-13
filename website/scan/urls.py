from django.urls import path
from . import views

app_name = 'scan'
urlpatterns = [
    path('', views.index, name='scan'),
]