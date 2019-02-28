from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Patient, Scan, Diagnosis
from .models import PatientForm
from typing import Sequence
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter


"""
Search Bar
"""
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'scan/list.html', {'filter': user_filter})


    
def dashboard(request: HttpRequest):
	"""
	Doctor's dashboard
	- lists patients
	- Doctor information
	- additional information
	"""

	return render(request, 'dashboard.html', {

	})

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
	scan = Scan.objects.order_by('?').first()

	return render(request, 'viewer.html', {
		"patient": patient.toView() if patient else None,
		"scan": scan.toView() if scan else None,
	})

def edit(request, pid):
	patient = get_object_or_404(Patient, pk=pid)
	if request.method == 'POST':
		form = PatientForm(request.POST, instance=patient)
		if form.is_valid():
			form.save()
			return redirect(reverse('scan:patients'))
	else:
		form = PatientForm(instance=patient)
	return render(request, 'patient/edit.html', {'form':form})

def add(request):
	if request.method == 'POST':
		form = PatientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('scan:patients'))
	else:
		form = PatientForm()
	return render(request, 'patient/edit.html', {'form':form})

def delete(request, pid):
	patient = get_object_or_404(Patient, pk=pid)
	form = PatientForm(instance=patient)
	if request.method == 'POST':
		patient.delete()
		return redirect(reverse('scan:patients'))
	else:
		return render(request, 'patient/delete.html', {'form':form})

def view(request, pid):
	obj = Patient.objects.filter(pk=pid).first()
	form = PatientForm(instance=obj)
	return render(request, 'patient/view.html', {'form':form})