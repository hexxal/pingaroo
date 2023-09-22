import os
import logging

import requests

from celery import Celery
from celery import shared_task
from celery.signals import worker_ready
from celery.schedules import crontab


LOG = logging.getLogger(__name__)

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'local_settings')

app = Celery('pingaroo')


# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all cqelery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://:foobar@redis:6379/0'
app.conf.broker_connection_retry_on_startup = True

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, monitor_targets.s(), name='initialize_attach_monitors')


@app.task
def monitor_targets():
    try:
        from pingaroo.models import MonitorResult, MonitorTarget
        for target in MonitorTarget.objects.all():
            LOG.info(f"Monitoring {target.url}")
            response = requests.get(target.url)
            latency = None
            if response.ok:
                latency = response.elapsed.total_seconds()
            MonitorResult.objects.create(target=target, is_down=response.ok, latency=latency)
            LOG.info(f"{target.url} in {latency}")
    except Exception as e:
        LOG.error('monitor_target error: %s', e)

