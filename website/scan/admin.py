from django.contrib import admin
from scan.models import Patient, Scan

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
	list_display =  [f.name for f in Patient._meta.fields]
	search_fields = [f.name for f in Patient._meta.fields]

class ScanAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Scan._meta.fields]
	search_fields = [f.name for f in Scan._meta.fields]

"""class DiagnosisAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Diagnosis._meta.fields]
	search_fields = [f.name for f in Diagnosis._meta.fields]"""

admin.site.register(Patient, PatientAdmin)
admin.site.register(Scan, ScanAdmin)
"""admin.site.register(Diagnosis, DiagnosisAdmin)"""
