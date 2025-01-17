from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    department_count = serializers.IntegerField(read_only=True)
    employee_count = serializers.IntegerField(read_only=True)
    project_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'department_count', 'employee_count', 'project_count']
        read_only_fields = ('created_at', 'updated_at')