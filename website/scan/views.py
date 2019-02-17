from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse
from .models import Patient, Scan, Diagnosis
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
