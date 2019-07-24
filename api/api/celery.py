import os
from celery import Celery
from configurations import importer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.config')


importer.install()

app = Celery('api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
