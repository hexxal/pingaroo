from django.db import models

class MonitorTarget(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class MonitorResult(models.Model):
    is_down = models.BooleanField()
