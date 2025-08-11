from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_view, name='product-view'),
    path('category', views.category_view, name='category-view'),
]