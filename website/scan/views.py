from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Patient, Scan, Diagnosis


def index(request):
	"""
	List of scans
	"""

	params = {}

	return render(request, 'index.html', params)


def change(request):
	"""
	TEST PAGE
	"""

	return render(request, 'upload_form.html')

def test(request):
	"""
	TEST PAGE
	"""

	#
	patient = Patient.objects.order_by('?').first()

	return render(request, 'upload_form.html', {"patient": patient})
