from django.forms import ModelForm
from django import forms

from scan.models import Patient, Scan


class DateInput(forms.DateInput):
    input_type = 'date'


class PatientForm(ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    Chemo = forms.BooleanField()
    smoker = forms.BooleanField()
    diabetes = forms.BooleanField()
    insulin = forms.BooleanField()

    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'birth_date': DateInput(),
            'Last_Chemo': DateInput()
        }


class ScanForm(ModelForm):
    class Meta:
        model = Scan
        fields = ['sid','diag_date','diagnosis','reason', 'file']
        widgets = {
            'diag_date': DateInput()
        }
