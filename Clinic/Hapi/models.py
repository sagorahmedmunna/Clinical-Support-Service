from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Extend Django's User model to add role and FHIR ID
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    fhir_id = models.CharField(max_length=100, unique=True)  # ID from HAPI FHIR server

    # Fix the conflict by adding a unique related_name
    groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)

    def __str__(self):
        return f"{self.username} - {self.role}"
