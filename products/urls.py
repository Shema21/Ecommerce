from django.urls import path
from .views import ProductListCreateView, CategoryListCreateView, ProductRetrieveUpdateDestroyView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail-update'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
]

