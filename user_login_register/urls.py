from django.urls import path
from .views import signup, email_activate, say_hello, hvv, async_view  # get_celery_worker_status





urlpatterns = [
    path('sig/', signup),
    path('hc/', hvv),
    path('av/', async_view),
    # path('sinm/', get_celery_worker_status),
    path('get/', say_hello),
    path('activate/<str:uidb64>/<str:token>', email_activate, name='activate'),
]
