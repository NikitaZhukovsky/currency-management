import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financial.settings')

app = Celery("financial")
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-1-minute': {
        'task': 'management.tasks.add_to_db',
        'schedule': crontab(minute='0', hour='*/3')
    },
}