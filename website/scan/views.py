from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Patient, Scan
from .forms import PatientForm, ScanForm
from typing import Sequence
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

@login_required(login_url='login:login')
def dashboard(request: HttpRequest):
    """
    Doctor's dashboard
    - lists patients
    - Doctor information
    - additional information
    """

    return render(request, 'dashboard.html', {

    })


@login_required(login_url='login:login')
def patient_list(request: HttpRequest):
    """
    List of patients
    """
    if 'Search' in request.GET:
        search = request.GET.get('Search')
        patients: Sequence[Patient] = Patient.objects.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search))
    else:
        patients: Sequence[Patient] = Patient.objects.all()

    return render(request, 'patient/list.html', {
        'patients': patients
    })


@login_required(login_url='login:login')
def view(request, pid):
    """
    View patient information
    """
    patient = Patient.objects.filter(pk=pid).first()

    scans = Scan.objects.filter(patient=pid)

    return render(request, 'patient/view.html', {'patient': patient, 'scans': scans, 'pid': pid})


@login_required(login_url='login:login')
def edit(request, pid):
    """
    Edit patient information
    using form in patient/edit.html
    """
    patient = get_object_or_404(Patient, pk=pid)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect(reverse('scan:view', kwargs={'pid': pid}))
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/edit.html', {'form':form})


@login_required(login_url='login:login')
def add(request):
    """
    Add new patient
    using form in patient/edit.html
    """
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('scan:patients'))
    else:
        form = PatientForm()
    return render(request, 'patient/edit.html', {'form':form})


@login_required(login_url='login:login')
def delete(request, pid):
    """
    Delete patient
    using form in patient/delete.html
    """
    patient = get_object_or_404(Patient, pk=pid)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        patient.delete()
        return redirect(reverse('scan:patients'))
    else:
        return render(request, 'patient/delete.html', {'form':form})



@login_required(login_url='login:login')
def scan_list(request: HttpRequest):
    """
    List of scans
    """

    scans: Sequence[Scan] = Scan.objects.all()

    return render(request, 'scan/list.html', {
        'scans': scans
    })


@login_required(login_url='login:login')
def edit_scan(request, sid):
    """
    Edits scan with form

    :param sid: scan id
    :return:
    """

    scan = get_object_or_404(Scan, pk=sid, doctor=request.user)
    pid = scan.patient.pid
    if request.method == 'POST':
        form = ScanForm(request.POST, request.FILES, instance=scan)
        if form.is_valid():
            diag_date = form.cleaned_data['diag_date']
            birth_date = get_object_or_404(Patient, pk=pid).birth_date
            if diag_date < birth_date or diag_date > datetime.date.today():
                messages.error(request, 'Date should be between birthday and today!')
                return render(request, 'scan/edit_scan.html', context={'form':form, 'pid':pid})
            form.save()
            return redirect(reverse('scan:view', kwargs={'pid': pid}))
    else:
        form = ScanForm(instance=scan)
    return render(request, 'scan/edit_scan.html', {'form': form, 'pid': pid})


@login_required(login_url='login:login')
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
            if new_scan.diag_date < new_scan.patient.birth_date or new_scan.diag_date > datetime.date.today():
                messages.error(request, 'Date should be between birthday and today!')
                return render(request, 'scan/edit_scan.html', context={'form':form, 'pid':pid})
            new_scan.doctor = request.user
            new_scan.save()
            return redirect(reverse('scan:view', kwargs={'pid': pid}))
    else:
        form = ScanForm()
    return render(request, 'scan/edit_scan.html', {'form':form, 'pid': pid})


@login_required(login_url='login:login')
def delete_scan(request, sid):
    """
    Deletes scan (with confirmation message)

    :param sid: scan id
    :return:
    """

    scan = get_object_or_404(Scan, pk=sid, doctor=request.user)
    form = ScanForm(instance=scan)
    pid = scan.patient.pid
    
    if request.method == 'POST':
        scan.delete()
        return redirect(reverse('scan:view', kwargs={'pid': pid}))
    else:
        return render(request, 'scan/delete_scan.html', {'form':form, 'pid': pid})


@login_required(login_url='login:login')
def view_scan(request, pid, sid):
    """
    Shows scan page with some patient information

    :param pid: patient id
    :param sid: scan id
    :return:
    """

    scan: Scan = get_object_or_404(Scan, patient__pk=pid, pk=sid)

    return render(request, 'scan/view_scan.html', {'scan': scan, 'pid': pid})

@login_required(login_url='login:login')
def charts(request):
    """
    Render charts page
    """
    return render(request, 'stat/charts.html')
