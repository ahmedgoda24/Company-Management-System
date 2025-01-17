from django.db import models

from common.models import TimeStampedModel
from company.models import Company
# Create your models here.
class Department(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)

    @property
    def employee_count(self):
        return self.employees.count()

    @property
    def project_count(self):
        return self.projects.count()
    
    def __str__(self):
        return self.name