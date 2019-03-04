from django.contrib import admin
from login.models import DoctorUser

# Register your models here.
class DoctorUserAdmin(admin.ModelAdmin):
	list_display =  ['username', 'first_name', 'last_name', 'email']
	search_fields = ['username', 'first_name', 'last_name', 'email']

admin.site.register(DoctorUser, DoctorUserAdmin)

#admin.site.register(DoctorUser)