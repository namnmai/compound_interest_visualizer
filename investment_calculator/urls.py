from django.urls import path
from . import views

urlpatterns = [
    # Change the path for 'calculate_investment' to be the root URL
    path('', views.calculate_investment, name='calculate_investment'),
    # Update the path for the 'about' page if necessary
    path('about/', views.about, name='about'),
    # Add other URL patterns here if necessary
    path('faq/', views.faq, name='faq'),
]
