from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsEmployee, IsManager , IsAdmin 
from rest_framework.decorators import action
from .models import Employee, PerformanceReview
from .serializers import EmployeeSerializer, PerformanceReviewCreateSerializer,PerformanceReviewSerializer
from rest_framework.response import Response
from rest_framework import status


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
   

    def get_permissions(self):
        if self.action in ['create','update','partial_update','destroy']:
            permission_classes = [IsManager]
        else:
           permission_classes = [IsAuthenticated, IsEmployee]
        return [permission() for permission in permission_classes]




class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update','destroy']:
            return PerformanceReviewCreateSerializer
        else:
            return PerformanceReviewSerializer
        

    @action(detail=True, methods=['post'])
    def transition(self, request, pk=None):
        review = self.get_object()
        new_stage = request.data.get('new_stage')

        if not new_stage:
            return Response(
                {'error': 'New stage is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not review.can_transition_to(new_stage):
            return Response(
                {'error': 'Invalid stage transition'},
                status=status.HTTP_400_BAD_REQUEST
            )

        review.current_stage = new_stage
        review.save()

        return Response(PerformanceReviewSerializer(review).data)