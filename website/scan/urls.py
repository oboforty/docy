from django.urls import path
from . import views

app_name = 'scan'
urlpatterns = [
    path('', views.index, name='scan'),
    path('upload_form/', views.change, name='upload_form'),
    path('test/', views.test, name='test'),
]
