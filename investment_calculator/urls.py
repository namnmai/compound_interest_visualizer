from django.urls import path
from . import views

urlpatterns = [
    # Change the path for 'calculate_investment' to be the root URL
    path('', views.calculate_investment, name='calculate_investment'),
]
