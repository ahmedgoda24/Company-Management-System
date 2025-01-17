from django.db import models
from django.utils import timezone
from company.models import Company
from department.models import Department
from django.core.validators import EmailValidator, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from common.models import TimeStampedModel
# Create your models here.
class Employee(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()
    designation = models.CharField(max_length=100)
    hired_on = models.DateField(null=True, blank=True)
    
    @property
    def days_employed(self):
        if self.hired_on:

            return (timezone.now().date() - self.hired_on).days
        return None

    def __str__(self):
        return self.name

class PerformanceReview(TimeStampedModel):
    REVIEW_STATES = [
        ('PENDING', 'Pending Review'),
        ('SCHEDULED', 'Review Scheduled'),
        ('FEEDBACK', 'Feedback Provided'),
        ('UNDER_APPROVAL', 'Under Approval'),
        ('APPROVED', 'Review Approved'),
        ('REJECTED', 'Review Rejected'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    current_state = models.CharField(
        max_length=20,
        choices=REVIEW_STATES,
        default='PENDING'
    )
    review_date = models.DateTimeField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    

    def can_transition_to(self, new_state):
        transitions = {
            'PENDING': ['SCHEDULED'],
            'SCHEDULED': ['FEEDBACK'],
            'FEEDBACK': ['UNDER_APPROVAL'],
            'UNDER_APPROVAL': ['APPROVED', 'REJECTED'],
            'REJECTED': ['FEEDBACK'],
            'APPROVED': [],
        }
        return new_state in transitions.get(self.current_state, [])
    

