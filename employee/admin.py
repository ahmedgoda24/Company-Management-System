from django.contrib import admin

from .models import Employee ,PerformanceReview

# Register your models here.
admin.site.register(Employee)
admin.site.register(PerformanceReview)

