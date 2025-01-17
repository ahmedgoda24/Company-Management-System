from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.IntegerField(read_only=True)
    project_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'company', 'name', 'employee_count', 'project_count']
        read_only_fields = ('created_at', 'updated_at')