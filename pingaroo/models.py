from django.db import models

class MonitorTarget(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class MonitorResult(models.Model):
    target = models.ForeignKey(MonitorTarget, on_delete=models.CASCADE)
    is_down = models.BooleanField()
    latency = models.DecimalField(max_digits=5, decimal_places=3)

    def __str__(self):
        return self.target.url