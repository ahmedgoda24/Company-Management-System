from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (EmployeeViewSet,PerformanceReviewViewSet
)
router = DefaultRouter()

router.register('employees', EmployeeViewSet)
router.register('reviews', PerformanceReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]