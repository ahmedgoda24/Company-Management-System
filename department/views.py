from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsEmployee, IsManager , IsAdmin 
from .models import Department
from .serializers import DepartmentSerializer

# Create your views here.
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.select_related('company')  
    serializer_class = DepartmentSerializer
  
    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            permission_classes = [IsManager]
        else:
           permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]
    
   