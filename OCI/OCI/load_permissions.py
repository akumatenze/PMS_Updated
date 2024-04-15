# management/commands/load_permissions.py

import json
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from guardian.shortcuts import assign_perm # type: ignore
from .models import CustomPermission  # type: ignore # Import your CustomPermission model

class Command(BaseCommand):
    help = 'Load permissions from JSON file'

    def handle(self, *args, **options):
        # Load permissions from JSON file
        with open('path/to/permissions.json', 'r') as file:
            data = json.load(file)

        # Create or retrieve groups for different user roles
        staff_group, created = Group.objects.get_or_create(name='Staff')
        user_group, created = Group.objects.get_or_create(name='User')

        # Assign permissions to groups
        staff_permissions = CustomPermission.objects.filter(codename__in=['can_view_dashboard', 'can_edit_dashboard'])
        user_permissions = CustomPermission.objects.filter(codename='can_view_dashboard')

        staff_group.permissions.set(staff_permissions)
        user_group.permissions.set(user_permissions)

        # Create or retrieve users
        staff_user, created = User.objects.get_or_create(username='staff_user')
        user_user, created = User.objects.get_or_create(username='user_user')

        # Assign groups to users
        staff_user.groups.add(staff_group)
        user_user.groups.add(user_group)

        # Assign permissions to users
        staff_user.user_permissions.set(staff_permissions)
        user_user.user_permissions.set(user_permissions)

        self.stdout.write(self.style.SUCCESS('Permissions loaded successfully'))

# Define custom permissions
from django.db import models

class CustomPermission(models.Model):
    name = models.CharField(max_length=255)
    codename = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Custom Permission'
        verbose_name_plural = 'Custom Permissions'
