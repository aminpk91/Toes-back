from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
import random
from Toest.celery import app


# @shared_task(name="send_mail")
# def async_send_mail(mail_subject, message):
#     send_mail(mail_subject, message, settings.EMAIL_HOST_USER, ["toestco@gmail.com"])


@app.task(bind=True)
def async_send_mail(self, mail_subject, message, l_email):
    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, l_email)
    if not cache.get(f"code:{id}"):
        code = random.randint(10000, 99999)
        cache.set(f"code:{id}", code, 2 * 60)

    print(f'task is   <=============>  \n  {mail_subject} \n\n{message} \n\n\n\n {settings.EMAIL_HOST_USER}')
    # print('Request: {0!r}'.format(self.request))
    return code
#

@shared_task
def async_cache():
    print("hellooooooooooooooooooooooooooooooooooo")
    if not cache.get(f"code:{id}"):
        code = random.randint(1, 999)
        cache.set('aaaaaaaaaaaaaallllll', code)
        cache.set(f"code:{id}", code, 2 * 60)
    return code


@app.task(bind=True)
def set_cashe(self, xam):
    print('setcacheeeeeeeeeeeeeeeeee')
    x = random.randint(1, 999)
    cache.set(f'code:{x}', x)
    cache.set('aaaaaaaaaaaaaallllll', 2222)
    cache.set(f'code:{xam}', xam)
    print('Request: {0!r}'.format(self.request))
    return print('ooooooooooooooooooooooo')
