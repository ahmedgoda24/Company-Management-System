from django.shortcuts import render
from rest_framework import viewsets

from authentication.permissions import IsAdmin, IsManager
from company.models import Company
from company.serializers import CompanySerializer

# Create your views here.
class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = Company.objects.all()
        serializer_class = CompanySerializer
        permission_classes = [IsManager]
    