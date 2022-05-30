import json
import asyncio
from time import sleep
import httpx
from django.http import HttpResponse
import random
from django.core.cache import cache
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from Utils.account_token import account_activation_token
from django.views.generic import View
from .tasks import async_send_mail, async_cache, set_cashe

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

User = get_user_model()


async def http_call_async():
    for num in range(1, 20):
        await asyncio.sleep(1)
        print(num)
        async with httpx.AsyncClient() as client:
            r = await client.get("https://httpbin.org")
            print(r)


import asyncio


async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def main():
    # await asyncio.gather(count(), count(), count())
    done, pending = await asyncio.wait(count())
    if done:
        print('congra')


def hvv(request):
    asyncio.run(main())
    return HttpResponse('Non-blocking HTTP request')


async def hv(request):
    # loop = asyncio.get_event_loop()
    # loop.create_task(main())
    return HttpResponse('Non-blocking HTTP request')


#
# if __name__ == "__main__":
#     import time
#
#     s = time.perf_counter()
#     asyncio.run(main())
#     elapsed = time.perf_counter() - s
#     print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# async def foo():
#     await asyncio.sleep(5)
#     print("after 5 secend in def")
#
#
# task = asyncio.create_task(foo())
# print(task)
# done, pending = await asyncio.wait(task)
#
# if task in done:
#     # Everything will work as expected now.
#     print("task done retend")
#     # asyncio.create_task(foo())


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')


@csrf_exempt
@require_http_methods(["POST"])
def signup(request):
    # # print(request.GET.get('COOKIE', None))
    # print(get_token(request))
    # tok = get_token(request)
    # ms = {"mss": f"{get_token(request)}"}
    # return JsonResponse(ms)
    # print(request.GET.get('COOKIE', None))
    if request.method == "POST":
        print("oooooooooooooooooooooook1")
        print(request.body.decode('utf-8'))
        body = request.body.decode('utf-8')
        body_val = json.loads(body)
        email = body_val.get("email", None)
        print(type(email))
        l_email = [email]
        print(l_email)
        phone = body_val.get("phone", None)
        if email:
            if User.objects.filter(email__iexact=email).count() == 0:
                password = body_val.get('password', None)
                repeated_passweord = body_val.get('repeat_password', None)
                print("oooooooooooooooooooooook2")
                if password:
                    if password == repeated_passweord:
                        try:
                            user = User.objects.create_user(email=email, password=password, phone=phone,
                                                            is_active=False)
                            print("oooooooooooooooooooooook3")
                            current_site = get_current_site(request)
                            mail_subject = 'Activate your account in Toest.'
                            message = render_to_string('validation_email_template.html', {
                                'user': user,
                                'domain': current_site.domain,
                                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                'token': account_activation_token.make_token(user),
                            })
                            # to_email = request.POST.get('email')
                            # print(to_email)
                            # to_email = list(to_email)
                            # print(to_email)

                            # send_mail(mail_subject, message, settings.EMAIL_HOST_USER, ["python.ekbatan@gmail.com"])
                            print("oooooooooooooooooooooook4")
                            async_send_mail.delay(mail_subject, message, l_email)
                            print("oooooooooooooooooooooook5")
                            return HttpResponse('Please confirm your email address to complete the registration')
                            messages.success(request, "Register Successfully!")
                            return HttpResponse('Please confirm your email address to complete the registration')
                        except IntegrityError as e:
                            # return render(request, "user/error.html", {"message": e})
                            messages.error(request, f"{e}")
                            return HttpResponse('Please confirm your email address to complete the registration')
                    else:
                        return HttpResponse("pass va tekraresh equal nistan")
            else:
                return HttpResponse("email tekrari")
        else:
            return HttpResponse("just post method")


def email_activate(request, uidb64, token):
    # User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.activate = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@csrf_exempt
def say_hello(request):
    print("berfore")

    # async_cache.delay()
    # print('setcache')
    x = random.randint(1, 999)
    m = set_cashe.delay(x)

    print('this is MMMM')
    print(m)
    print('------------------')
    print(m.status)
    print('------------------')
    print(m.id)
    print('------------------')
    print('this is xxxxx')
    print(x)
    # cache.set('thiss iss', x)
    print("after")
    print(m.status)
    return HttpResponse('Thank you for your email confirmation. Now you can login your account.')

# @csrf_exempt
# @require_http_methods(["POST"])
# def get_celery_worker_status():
#     async_cache.delay()
#     # ERROR_KEY = "ERROR"
#     # try:
#     #     from celery.task.control import inspect
#     #     insp = inspect()
#     #     d = insp.stats()
#     #     if not d:
#     #         d = { ERROR_KEY: 'No running Celery workers were found.' }
#     # except IOError as e:
#     #     from errno import errorcode
#     #     msg = "Error connecting to the backend: " + str(e)
#     #     if len(e.args) > 0 and errorcode.get(e.args[0]) == 'ECONNREFUSED':
#     #         msg += ' Check that the RabbitMQ server is running.'
#     #     d = { ERROR_KEY: msg }
#     # except ImportError as e:
#     #     d = { ERROR_KEY: str(e)}
#     return print("ok ok ok")
