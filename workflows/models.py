from django.db import models


class WorkflowStatus(models.IntegerChoices):
    """Statuses of a workflow step"""

    SUCCESS = 0
    DATA_ERROR = 1
    SYSTEM_ERROR = 2


class Workflow(models.Model):
    """Model for the defintion of a workflow"""

    name = models.CharField(max_length=64)
    # author = models.ForeignKey("users.User", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    """Model for the definition of a step in a workflow"""

    name = models.CharField(max_length=64)
    workflow = models.ForeignKey(
        Workflow, related_name="steps", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def last_attempt_status(self):
        """Retrieve the last attempt status for the current Step object"""

        attempts = self.attempts.all()
        return attempts.latest("created_at").status if attempts else None

    def __str__(self):
        return self.name


class Attempt(models.Model):
    """Model for the storage of an attempt to run a workflow step"""

    step = models.ForeignKey(Step, related_name="attempts", on_delete=models.CASCADE)
    source = models.URLField(null=True, blank=True)
    status = models.IntegerField(choices=WorkflowStatus.choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = "created_at"
