from django.contrib.auth.models import AbstractUser
from django.db import models


# ----------------------------------------------------------
# USER (base = email, Fname, Lname)
class CustomUser(AbstractUser):
    date_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    full_address = models.TextField(blank=True)

    def __str__(self):
        return self.email
