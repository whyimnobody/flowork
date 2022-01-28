import pytest

from ..models import Attempt, Step, Workflow, WorkflowStatus


@pytest.mark.django_db
def test_get_last_attempt_status():
    # TODO: Replace below object creations with mock objects
    workflow = Workflow.objects.create(name="Test Workflow")
    step = Step.objects.create(name="Test Step", workflow=workflow)
    _ = Attempt.objects.create(step=step, status=WorkflowStatus.DATA_ERROR.value)
    good_attempt = Attempt.objects.create(
        step=step, status=WorkflowStatus.SUCCESS.value
    )

    assert step.last_attempt_status == good_attempt.status


@pytest.mark.django_db
def test_get_last_attempt_no_attempt():
    workflow = Workflow.objects.create(name="Test Workflow")
    step = Step.objects.create(name="Test Step", workflow=workflow)

    assert step.last_attempt_status == None
