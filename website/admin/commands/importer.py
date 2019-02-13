import csv

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Imports hospital excel file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        for filename in options['file']:

            # parse CSV
            with open(filename, 'r') as csvfile:
                spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
                
                # go through each line
                for row in spamreader:
                    print(row)
                    break


            # done
            self.stdout.write(self.style.SUCCESS('Successfully imported file "%s"' % file))