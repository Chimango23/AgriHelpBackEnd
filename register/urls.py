from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.farmers_detail),
    path('', views.farmers_list),
]