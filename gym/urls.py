from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/submit/', views.submit_contact_request, name='submit_contact_request'),
]
