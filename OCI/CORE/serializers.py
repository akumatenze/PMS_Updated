# core/serializers.py
from rest_framework import serializers
from .models import Tenancy, Region, Profile, Compartment

class TenancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenancy
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CompartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartment
        fields = '__all__'


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


from rest_framework import serializers
from .models import Tenancy, Region, Profile, Compartment

class TenancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenancy
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CompartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compartment
        fields = '__all__'
