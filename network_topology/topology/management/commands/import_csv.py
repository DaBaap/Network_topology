import csv
from django.core.management.base import BaseCommand
from topology.models import LLDP  

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                LLDP.objects.create(
                    device_a_name=row['Device_A_Name'],
                    device_a_interface=row['Device_A_Interface'],
                    device_a_ip=row['Device_A_IP'],
                    device_b_name=row['Device_B_Name'],
                    device_b_interface=row['Device_B_Interface'],
                    device_b_ip=row['Device_B_IP']
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully!!'))
