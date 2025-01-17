from rest_framework import serializers
from .models import Employee ,PerformanceReview
class EmployeeSerializer(serializers.ModelSerializer):
    days_employed = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class EmpolyeeListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Employee
        fields = ['id','name','email','department','mobile_number',]
        

class PerformanceReviewSerializer(serializers.ModelSerializer):
    employee=EmpolyeeListSerializer(read_only=True)
    class Meta:
        model = PerformanceReview
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class PerformanceReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')