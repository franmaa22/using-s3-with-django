from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=200, unique=True)

class Station(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="stations")
    name = models.CharField(max_length=200)

class Log(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="logs")
    name = models.CharField(max_length=200)