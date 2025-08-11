from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('category', views.category_view, name='category-view'),
]