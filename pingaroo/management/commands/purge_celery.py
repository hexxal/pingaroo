from django.core.management.base import BaseCommand, CommandError
from project.celery import app as celery_app


class Command(BaseCommand):
    help = "Purge all Celery tasks"

    def handle(self, *args, **options):
        purged_count = celery_app.control.purge()
        self.stdout.write(self.style.SUCCESS('Successfully purged "%d" tasks' % purged_count))
