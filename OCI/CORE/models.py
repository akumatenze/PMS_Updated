# core/models.py
from django.db import models

class Tenancy(models.Model):
    name = models.CharField(max_length=100)

class Region(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField('account.User', on_delete=models.CASCADE)
    # Add other fields as needed

class Compartment(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed


# Create your models here.
    
    
# OCI/models.py

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tenancy(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=100)
    tenancy = models.ForeignKey(Tenancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Compartment(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class KeyFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='keyfiles/')

    def __str__(self):
        return self.name

# models.py in the respective apps (staff, users, login, logout, signup, profile)

from django.db import models

class Staff(models.Model):
    # Define your staff model fields here
    pass

class User(models.Model):
    # Define your user model fields here
    pass

class Login(models.Model):
    # Define your login model fields here
    pass

class Logout(models.Model):
    # Define your logout model fields here
    pass

class Signup(models.Model):
    # Define your signup model fields here
    pass

class Profile(models.Model):
    # Define your profile model fields here
    pass


from django.db import models

class Tenancy(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

class Region(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

class Profile(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

class Compartment(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as necessary

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add fields as needed
    oci_user_id = models.CharField(max_length=100, blank=True)
    oci_credentials = models.JSONField(blank=True, null=True)

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add fields as needed
    oci_user_id = models.CharField(max_length=100, blank=True)
    oci_credentials = models.JSONField(blank=True, null=True)

class Tenancy(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Region(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Compartment(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
