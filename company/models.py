from django.db import models
from common.models import TimeStampedModel
# Create your models here.
class Company(TimeStampedModel):
    name = models.CharField(max_length=255)

    @property
    def department_count(self):
        return self.departments.count()
    
    @property
    def employee_count(self):
        return self.employees.count()

    @property
    def project_count(self):
        return self.projects.count()
    
    def __str__(self):
        return self.name
