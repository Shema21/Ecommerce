from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce API",
        default_version='v1',
        description="API for E-Commerce Platform",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/store/', include('products.urls')),
    path('api/apikey/', include('apikeys.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
