from django.db import models
from django.core.validators import RegexValidator


class Employee(models.Model):

    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=16, unique=True)
    address = models.TextField()
