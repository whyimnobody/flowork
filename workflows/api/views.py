from rest_framework import viewsets

from .serializer import WorkflowReportSerializer

from ..models import Attempt


class WorkflowReportViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset of GET methods for retrieving a workflow report"""

    def get_queryset(self):
        """
        Optionally restrict the number of records in the report, by filtering
        with a date range in the query parameters of the request.
        """
        queryset = Attempt.objects.all().select_related("step", "step__workflow")

        start_date = self.request.query_params.get("start")
        end_date = self.request.query_params.get("end")

        if start_date and end_date:
            queryset = queryset.filter(created_at__range=[start_date, end_date])
        elif start_date:
            queryset = queryset.filter(created_at__gte=start_date)
        elif end_date:
            queryset = queryset.filter(created_at__lte=end_date)
        return queryset

    serializer_class = WorkflowReportSerializer
