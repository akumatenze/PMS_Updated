from django.db import models
# account/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add custom fields here
    pass
class User(AbstractUser):
    # Custom fields
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    # Add more custom fields as needed
