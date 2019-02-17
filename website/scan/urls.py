from django.urls import path
from . import views

app_name = 'scan'
urlpatterns = [
    # path('', views.index, name='dashboard'),

    path('scans/', views.scan_list, name='scans'),
    path('patients/', views.patient_list, name='patients'),

    path('upload_form/', views.change, name='upload_form'),
    path('test/', views.test, name='test'),


]
