from django.shortcuts import render, redirect, reverse
from .models import Patient, Scan, Diagnosis

# Create your views here.
def index(request):
	params = {}

	return render(request,'index.html', params)

def change(request):
	return render(request,'patient.html')