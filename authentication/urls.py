from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from authentication import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),  # Renamed jwt-create
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),  # Optional: Keep this
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),  # Optional: Keep this
]
