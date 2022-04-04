from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView


app_name = 'agents'

urlpatterns = [
    path("Agent_list/", AgentListView.as_view(), name="agent_list"),
    path("Agent_create/", AgentCreateView.as_view(), name="agent_create"),
    path("Agent_details/<int:pk>", AgentDetailView.as_view(), name="agent_details"),
]
