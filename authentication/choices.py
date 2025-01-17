from django.db import models
class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', 'admin'
    MANAGER = 'MANAGER', 'manager'
    EMPLOYEE = 'EMPLOYEE', 'employee'

