import codecs
import csv
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from scan.models import Patient


class Command(BaseCommand):
    help = 'Imports hospital excel file into the database'

    def add_arguments(self, parser):
        default_file_loc = '../_dev/files/Dataset.csv'

        parser.add_argument('file', nargs='?', type=str, default=default_file_loc)

    def try_parsing_date(text):
        print("hi")
        for fmt in ( '%d/%m/%Y', '%Y', '%m/%Y'):
            try:
                return datetime.strptime(text, fmt)
            except:
                pass

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
            'Last Diagnosis',
            'Smoker',
            'PACKS YEAR',
            'Diabetes',
            'Insulin',
            'Result'
        ]

        # parse CSV
        with codecs.open(filename, 'r', encoding='utf8') as csvfile:
            spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            i = 0
            # go through each line
            for row in spamreader:

                if i > 100:
                    break

                i += 1

                try:
                   
                    new_patient= Patient()
                    new_patient.age= int(row['Age'])
                    new_patient.birth_date= datetime.strptime(row['Date of Birth'],"%d/%m/%Y")
                    if row['Sex']=='ΑΝΔΡΑΣ':
                        new_patient.gender= 1
                    else:
                        new_patient.gender= 2
                    if row['Smoker'] == 'ΝΑΙ' :
                        new_patient.smoker= True
                        try:
                            new_patient.Packs_yearly= float(row['PACKS YEAR'])
                        except:
                            new_patient.smoker= False
                            pass
                    else:
                        new_patient.smoker= False
                    if row['Chemotherapy'] == 'ΝΑΙ' :
                        new_patient.Chemo= True
                        try:
                            new_patient.Last_Chemo= datetime.strptime(row['Last Diagnosis'],"%d/%m/%Y")
                        except:
                            new_patient.Chemo= False
                            pass
                    else:
                        new_patient.Chemo= False
                    if row['Diabetes'] == 'ΝΑΙ':
                        new_patient.diabetes= True
                        if row['Insulin'] == 'ΝΑΙ':
                            new_patient.insulin= True
                    else:
                        new_patient.diabetes= False
                        new_patient.insulin= False

                    new_patient.save()
                except Exception as e:
                    raise e


            # done
            self.stdout.write(self.style.SUCCESS('Successfully imported file "%s"' % filename))
