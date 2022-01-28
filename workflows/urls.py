from django.urls import path

from .views import WorkflowReportView


app_name = "workflow"
urlpatterns = [
    path("report", view=WorkflowReportView.as_view(), name="workflow_report"),
]
