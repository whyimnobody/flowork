from datetime import datetime
from django.http import StreamingHttpResponse
from django.views import generic

from .models import Attempt
from .utils import generate_csv_report


class WorkflowReportView(generic.TemplateView):
    def get(self, request, *args, **kwargs):

        data = Attempt.objects.all()
        print(data)
        print(generate_csv_report(data))
        return StreamingHttpResponse(
            generate_csv_report(data),
            content_type="text/csv",
            headers={
                "Content-Disposition": f'attachment; filename="workflow_report_{datetime.date}.csv"'
            },
        )
