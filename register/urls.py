from django.urls import path
from . import views
from . import login

urlpatterns = [
    path('<int:pk>/', views.farmers_detail),
    path('', views.farmers_list),
    path('login/',login.farmers_auth),
]