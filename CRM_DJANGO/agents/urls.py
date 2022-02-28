from django.urls import path
from .views import AgentListView, AgentCreateView


app_name = 'agents'

urlpatterns = [
    path("Agent_list/", AgentListView.as_view(), name="agent_list"),
    path("Agent_create/", AgentCreateView.as_view(), name="agent_create")
]
