import codecs
import csv
import time
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from login.models import DoctorUser
from scan.models import Patient, Scan


class Command(BaseCommand):
    """

    """

    help = 'Imports hospital csv file into the database. The csv file has to follow a strict format and be sorted by patients'

    def add_arguments(self, parser):
        default_file_loc = '../_dev/files/Dataset1.csv'

        parser.add_argument('file', nargs='?', type=str, default=default_file_loc)

    # def try_parsing_date(text):
    #     for fmt in ('%d/%m/%Y', '%Y', '%m/%Y'):
    #         try:
    #             return datetime.strptime(text, fmt)
    #         except:
    #             pass

    def create_scan(self, row, patient: Patient, doctor: DoctorUser):
        new_scan = Scan()
        new_scan.diag_date = datetime.strptime(row['Date Of Examination'], "%d/%m/%Y")
        new_scan.diagnosis = row[' Initial Diagnosis']
        new_scan.reason = row['Reason for Examination']
        new_scan.patient = patient
        new_scan.doctor = doctor

        return new_scan

    def create_patient(self, row):
        patient = Patient()
        patient.age = int(row['Age'])
        patient.birth_date = datetime.strptime(row['Date of Birth'], "%d/%m/%Y")

        # Sex determination
        if row['Sex'] == 'ΑΝΔΡΑΣ':
            patient.gender = 0
        else:
            patient.gender = 1

        if row['Smoker'] == 'ΝΑΙ':
            patient.smoker = True
            try:
                patient.Packs_yearly = float(row['PACKS YEAR'])
            except:
                patient.smoker = False
                pass
        else:
            patient.smoker = False
        if row['Chemotherapy'] == 'ΝΑΙ':
            patient.Chemo = True
            try:
                patient.Last_Chemo = datetime.strptime(row['Last Diagnosis'], "%d/%m/%Y")
            except:
                patient.Chemo = False
                pass
        else:
            patient.Chemo = False
        if row['Diabetes'] == 'ΝΑΙ':
            patient.diabetes = True
            if row['Insulin'] == 'ΝΑΙ':
                patient.insulin = True
        else:
            patient.diabetes = False
            patient.insulin = False

        return patient

    @transaction.atomic
    def handle(self, *args, **options):
        filename = options['file']

        doctor_default = DoctorUser.objects.get(username='docy')

        t_start = time.time()

        # bulk_scans = []
        # bulk_patients = []

        # parse CSV
        with codecs.open(filename, 'r', encoding='utf8') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

            oldcode= 'p'
            # go through each line
            for row in spamreader:
                try:
                    new_code= row["Patient Code"]

                    if oldcode==new_code:
                        scan = self.create_scan(row, patient, doctor_default)
                        scan.save()

                        oldcode = new_code
                    else:
                        patient = self.create_patient(row)
                        patient.save()

                        scan = self.create_scan(row, patient, doctor_default)
                        scan.save()

                        oldcode = new_code

                except Exception as e:
                    raise e
        t_end = time.time()

        # done
        self.stdout.write(self.style.SUCCESS('Successfully imported file "{}"\nTime took: {}'.format(filename, t_end - t_start)))
