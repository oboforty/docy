from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Patient, Scan
from .models import PatientForm, ScanForm
from typing import Sequence
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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
	if 'Search' in request.GET:
		search = request.GET.get('Search')
		patients: Sequence[Patient] = Patient.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))		
	else:
		patients: Sequence[Patient] = Patient.objects.all()
	
	return render(request, 'patient/list.html', {
		'patients': patients
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


def edit_scan(request, sid):
	"""
	Edits scan with form

	:param sid: scan id
	:return:
	"""

	scan = get_object_or_404(Scan, pk=sid)
	pid = scan.patient.pid
	if request.method == 'POST':
		form = ScanForm(request.POST, request.FILES, instance=scan)
		if form.is_valid():
			form.save()
			return redirect(reverse('scan:patients'))
	else:
		form = ScanForm(instance=scan)
	return render(request, 'scan/edit_scan.html', {'form':form, 'pid': pid})


def add_scan(request, pid):
	"""
	Adds scan with form

	:param pid: scan's parent patient id
	:return:
	"""

	if request.method == 'POST':
		form = ScanForm(request.POST, request.FILES)

		if form.is_valid():
			new_scan= form.save(commit= False)
			new_scan.patient = Patient.objects.filter(pk=pid).first()
			new_scan.save()
			return redirect(reverse('scan:view', kwargs={'pid': pid}))
	else:
		form = ScanForm()
	return render(request, 'scan/edit_scan.html', {'form':form, 'pid': pid})


def delete_scan(request, sid):
	"""
	Deletes scan (with confirmation message)

	:param sid: scan id
	:return:
	"""

	scan = get_object_or_404(Scan, pk=sid)
	form = ScanForm(instance=scan)
	pid = scan.patient.pid
	
	if request.method == 'POST':
		scan.delete()
		return redirect(reverse('scan:view', kwargs={'pid': pid}))
	else:
		return render(request, 'scan/delete_scan.html', {'form':form, 'pid': pid})


def view(request, pid):

	obj = Patient.objects.filter(pk=pid).first()
	form = PatientForm(instance=obj)

	scans = Scan.objects.filter(patient= pid)

	return render(request, 'patient/view.html', {'form':form, 'scans':scans, 'pid': pid})


#@login_required(login_url='login:login')
def view_scan(request, pid, sid):
	"""
	Shows scan page with some patient information

	:param pid: patient id
	:param sid: scan id
	:return:
	"""

	scan: Scan = get_object_or_404(Scan, patient__pk=pid, pk=sid)

	return render(request, 'scan/view_scan.html', {'scan': scan, 'pid': pid})
