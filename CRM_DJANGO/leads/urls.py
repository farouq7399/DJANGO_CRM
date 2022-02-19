from django.urls import path
from . import views

urlpatterns = [
    path('leads/', views.home_page, name="home_page"),
    path('leads/lead_details/<int:pk>', views.lead_detail, name="lead_details"),
    path('leads/lead_create/', views.create_lead, name="create_lead"),
]
