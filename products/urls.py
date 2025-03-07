from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.ListCreateProduct.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.GetUpdateProductDetails.as_view(), name='product-details-update'),
]