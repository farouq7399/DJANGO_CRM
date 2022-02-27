from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('leads/', views.home_page, name="home_page"),
    #path('leads/lead_create/', views.lead_create, name="create_lead"),
    #path('leads/lead_detail/<int:pk>', views.lead_detail, name="lead_details"),
    #path('leads/lead_update/<int:pk>', views.lead_update, name="update_lead"),
    #path('leads/lead_delete/<int:pk>', views.lead_delete, name="delete_lead"),
    # ===== This is start of the Class-Based Views
    path('login/', LoginView.as_view(), name="Login_leads"),
    path('logout/', LogoutView.as_view(), name="Logout_leads"),
    path('signup/', views.SignupView.as_view(), name="signup_user"),
    path('leads/', views.LeadListView.as_view(), name="home_page"),
    path('leads/create/', views.LeadCreateView.as_view(), name="create_lead"),
    path('leads/Details/<int:pk>', views.LeadDetailsView.as_view(), name="lead_details"),
    path('leads/update/<int:pk>', views.LeadUpdateView.as_view(), name="update_lead"),
    path('leads/delete/<int:pk>', views.LeadDeleteView.as_view(), name="delete_lead"),

]
