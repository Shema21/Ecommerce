from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, ProfileView, UserUpdateView, PasswordChangeView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='profile-update'),
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
]
