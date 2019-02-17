import codecs
import csv

from django.core.management.base import BaseCommand, CommandError

from scan.models import Patient


class Command(BaseCommand):
    help = 'Imports hospital excel file into the database'

    def add_arguments(self, parser):
        default_file_loc = '../_dev/files/Dataset.csv'

        parser.add_argument('file', nargs='?', type=str, default=default_file_loc)

    def handle(self, *args, **options):
        filename = options['file']

        headers = [
            'Date of Birth',
            'Sex',
            'Date Of Examination',
            'Age',
            'Reason for Examination',
            'Date Of Diagnosis',
            'Initial Diagnosis',
            'Chemotherapy',
            'Last Chemotherapy',
            'Smoker',
            'PACKS YEAR',
            'Diabetes',
            'Insulin',
            'Result'
        ]

        # parse CSV
        with codecs.open(filename, 'r', encoding='utf8') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

            # go through each line
            for row in spamreader:
                new_patient= Patient
                new_patient.age= int(row['Age'])
                new_patient.birth_date= row['Date Of Birth']
                new_patient.gender = row['Sex']
                new_patient.Packs_yearly= int(row['PACKS YEAR'])
                new_patient.Last_Chemo= row['Last Chemotherapy']
                if row['Smoker'] == :
                    new_patient.smoker= True
                if row['Chemotherapy'] == :
                    new_patient.Chemo= True
                if row['Chemotherapy'] == :
                    new_patient.Chemo= True


                break


        # done
        self.stdout.write(self.style.SUCCESS('Successfully imported file "%s"' % filename))
