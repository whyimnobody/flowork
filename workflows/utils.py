import csv

from django.db.models import Count, Q

from .models import Attempt, Workflow, WorkflowStatus


# https://docs.djangoproject.com/en/4.0/howto/outputting-csv/
class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def generate_csv_report(queryset=None):
    """Generate a CSV file, from a given Attempt queryset"""

    if not queryset:
        queryset = (
            Attempt.objects.filter(~Q(status=WorkflowStatus.SUCCESS))
            .select_related("step", "step__workflow")
            .order_by("id")
            .distinct("step__workflow__id")
            .annotate(
                steps_count=Count("step__workflow__steps"),
                attempts_count=Count("step__workflow__steps__attempts"),
            )
        )

    queryset = queryset.annotate(
        steps_count=Count("steps__id"),
        attempts_count=Count("steps__attempts"),
        last_attempt_status=Count("steps"),
    )
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    # Write headers
    writer.writerow(
        [
            "Workflow Name",
            "Final Workflow Attempt Status",
            "Number of Steps",
            "Number of Attempts",
        ]
    )
    # Write content
    for attempt in queryset:
        writer.writerow(
            [
                attempt.name,
                attempt.last_attempt_status,
                attempt.steps_count,
                attempt.attempts_count,
            ]
        )

    return writer
