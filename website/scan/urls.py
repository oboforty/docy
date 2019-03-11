from django.urls import path
from . import views
from django.conf.urls import url
from scan import views



app_name = 'scan'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('scans/', views.scan_list, name='scans'),
    path('patients/', views.patient_list, name='patients'),

    path('add/', views.add, name='add'),
    path('edit/<int:pid>/', views.edit, name='edit'),
    path('delete/<int:pid>/', views.delete, name='delete'),
    path('view/<int:pid>/', views.view, name='view'),

    path('add_scan/<int:pid>', views.add_scan, name='add_scan'),
    path('edit_scan/<int:sid>', views.edit_scan, name= 'edit_scan'),
    path('delete_scan/<int:sid>', views.delete_scan, name= 'delete_scan'),
    path('view_scan/<int:pid>/<int:sid>/', views.view_scan, name='view_scan'),
    path('charts/', views.charts, name='charts'),
]
