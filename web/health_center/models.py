from django.db import models
from django_google_maps.fields import AddressField, GeoLocationField


class HealthCenter(models.Model):
    name = models.CharField(max_length=255)
    address = AddressField(max_length=200)
    geolocation = GeoLocationField(blank=True)
