from django.urls import path
from .views import request_api_key

urlpatterns = [
    path('request/', request_api_key, name='request-api-key'),
]
