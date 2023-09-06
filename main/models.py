from django.db import models
from django.contrib.auth.models import AbstractUser
from jsonfield import JSONField

class Users(models.Model):
    json = JSONField(null=True)

class Vehicle(models.Model):
    json = JSONField(null=True)

