import os
from celery import Celery
from kombu.transport import redis
from Toest import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Toest.settings')

app = Celery('Toest')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()











# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Toest.settings.py')
# # BROKER_URL = 'redis://localhost:6379/0'
# BACKEND_URL = 'redis://localhost:6379/1'
# app = Celery('Toest', broker=BROKER_URL, backend=BACKEND_URL)




# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Toest.settings')

# app = Celery('Toest', broker=settings.CELERY_BROKER_URL)
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# app.autodiscover_tasks()
#
#
# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
#



# def get_celery_worker_status():
#     ERROR_KEY = "ERROR"
#     try:
#         from celery.task.control import inspect
#         insp = inspect()
#         d = insp.stats()
#         if not d:
#             d = { ERROR_KEY: 'No running Celery workers were found.' }
#     except IOError as e:
#         from errno import errorcode
#         msg = "Error connecting to the backend: " + str(e)
#         if len(e.args) > 0 and errorcode.get(e.args[0]) == 'ECONNREFUSED':
#             msg += ' Check that the RabbitMQ server is running.'
#         d = { ERROR_KEY: msg }
#     except ImportError as e:
#         d = { ERROR_KEY: str(e)}
#     return d
