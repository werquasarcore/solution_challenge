from django.urls import path
from . import views

urlpatterns = [
    path("reports/", views.reports),
    path("volunteers/", views.volunteers),
    path("tasks/priority/", views.priority_tasks),
    path("chatbot/ask/", views.chatbot),
    path("match/<int:report_id>/", views.match_worker),
    path("assign/", views.assign),
    path("assignments/", views.assignments),
    path("stats/", views.stats),
    path("update-status/", views.update_status),
]