from django.urls import path
from . import views

app_name = 'scan'
urlpatterns = [
    path('', views.index, name='scan'),
    path('patient/', views.display_random_patient, name='patient')
]