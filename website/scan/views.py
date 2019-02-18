from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from .models import Patient, Scan, Diagnosis
from .models import PatientForm
from typing import Sequence


# def index(request: HttpRequest):
# 	"""
# 	Doctor's dashboard
# 	- lists patients
#
# 	"""
#
#
#
# 	return render(request, 'index.html', {
#
# 	})

def scan_list(request: HttpRequest):
	"""
	List of scans
	"""

	scans: Sequence[Scan] = Scan.objects.all()

	return render(request, 'scan/list.html', {
		'scans': scans
	})

def patient_list(request: HttpRequest):
	"""
	List of patients
	"""


	patients: Sequence[Patient] = Patient.objects.all()

	return render(request, 'patient/list.html', {
		'patients': patients
	})

def change(request: HttpRequest):
	"""
	TEST PAGE
	"""

	return render(request, 'upload_form.html')

def test(request: HttpRequest):
	"""
	TEST PAGE
	"""

	#
	patient = Patient.objects.order_by('?').first()

	return render(request, 'upload_form.html', {"patient": patient})

def patient_list(request):
	entries = Patient.objects.all()
	return render(request, 'patient_list.html', {'patient_list':entries})

def edit(request, pid=-1):
	if pid != -1:
		obj = Patient.objects.filter(pk=pid).first()
	if request.method == 'POST':
		if pid != -1:
			form = PatientForm(request.POST, instance=obj)
		else:
			form = PatientForm(request.POST)#add
		if form.is_valid():
			form.save()
			return redirect(reverse('scan:patient_list'))
		return render(request, 'edit.html', {'form':form})
	else:
		if pid != -1:
			form = PatientForm(instance=obj)
		else:
			form = PatientForm()#add
		return render(request, 'edit.html', {'form':form})

def delete(request, pid):
	obj = Patient.objects.filter(pk=pid)
	obj.delete()
	return redirect(reverse('scan:patient_list'))