from django.db import models
from datetime import datetime

class BookingListIndi(models.Model):
    name_person = models.CharField(max_length=200)
    industry_name = models.CharField(max_length=100)
    date_visit = models.DateField(default=datetime.today())
    slots_present = models.IntegerField(default=0)
    visiting_members = models.IntegerField(default=0)
    street_name = models.CharField(max_length=150)
    city_name = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    code = models.CharField(max_length=20)
    visited = models.BooleanField(default=False)

class BookingListOrga (models.Model):
    name_person = models.CharField(max_length=200)
    organisation_name = models.CharField(max_length=200)
    industry_name = models.CharField(max_length=100)
    date_visit = models.DateField(default=datetime.today())
    slots_present = models.IntegerField(default=0)
    street_name = models.CharField(max_length=150)
    city_name = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    code = models.CharField(max_length=20)
    visited = models.BooleanField(default=False)