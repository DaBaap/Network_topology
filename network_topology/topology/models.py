# models.py
from django.db import models

class LLDP(models.Model):
    device_a_name = models.CharField(max_length=100)
    device_a_interface = models.CharField(max_length=50)
    device_a_ip = models.GenericIPAddressField()
    device_b_name = models.CharField(max_length=100)
    device_b_interface = models.CharField(max_length=50)
    device_b_ip = models.GenericIPAddressField()
