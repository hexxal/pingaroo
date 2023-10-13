from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True


class MonitorTarget(TimestampedModel):
    url = models.URLField()

    def __str__(self):
        return self.url


class MonitorResult(TimestampedModel):
    target = models.ForeignKey(MonitorTarget, on_delete=models.CASCADE, related_name='results')
    is_down = models.BooleanField()
    latency = models.IntegerField(null=True)

    def __str__(self):
        return self.target.url