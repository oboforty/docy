from django.shortcuts import render, redirect, reverse
from scan.models import Scan, Patient

# Create your views here.
def index(request):
	params = {}

	return render(request, 'index.html', params)


def display_random_patient(request):

	obj = Patient.objects

	return render(request, 'patient.html', {
		'obj': obj
	})
