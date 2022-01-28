from rest_framework import serializers

from ..models import Attempt


class WorkflowReportSerializer(serializers.ModelSerializer):
    """Serializer for a report of workflow attempts by step"""

    class Meta:
        model = Attempt
        fields = [
            "step__workflow__name",
            "step__name",
            "source",
            "status",
            "created_at",
        ]
