from django.shortcuts import render
import datetime

from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from Toest.settings import BASE_DIR
from .models import Photo, Subjects
from django.core.cache import cache
from .serializer import SubjectsSerializer, PhotoSerializer, Title_nested_Serializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication

from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework import permissions


@api_view()
@permission_classes((permissions.AllowAny,))
def hello_world(request):
    return Response({"message": "Hello, world!"})


@permission_classes((permissions.AllowAny,))
class redis_test(APIView):
    def get(self, request, format=None):
        cache.set(f"{self.request.user}", f"{datetime.datetime.now()}")
        cache.set(f"{self.request}", f"{datetime.datetime.now()}")
        usernames = {"user": f"{cache.get(f'{self.request.user}')}",
                     "request": f"{cache.get(f'{self.request}')}"}
        # usernames = {"second": f"WRGAVGERAEGVAERA"}

        return Response(usernames)
    # def post(self, request, format=None):
    #     snippets = {"salam": f"{timedelta.seconds}"}
    #     return Response(snippets.data)


class SubjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Subjects.objects.filter(active=True)
    serializer_class = SubjectsSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class Sidebar_ViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.filter(active=True).filter(index_sidebar=True)
    serializer_class = Title_nested_Serializer


class Product_ViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.filter(active=True).filter(product=True)
    serializer_class = Title_nested_Serializer


class Post_ViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.filter(active=True).filter(post_page=True)
    serializer_class = Title_nested_Serializer


# class PhotoViewSet(viewsets.ModelViewSet):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
#


@csrf_exempt
@permission_classes((permissions.AllowAny,))
def index(request):

    # cache.set("name", "ashkan", 50)
    # context = {"title": "صفحه اصلی", "name": "ashkan",
    #            "age": 19, "role": "customer"}
    qs = Subjects.objects.filter(active=True)
    qs2 = qs.filter(index_sidebar=True)
    context = {"sub": qs, "sidbar": qs2}
    return render(request, 'index.html', context)  # )


@csrf_exempt
@permission_classes((permissions.AllowAny,))
def aboute(request):
    # cache.set("name", "ashkan", 50)
    # context = {"title": "صفحه اصلی", "name": "ashkan",
    #            "age": 19, "role": "customer"}
    return render(request, 'about.html')  # , context)


@csrf_exempt
@permission_classes((permissions.AllowAny,))
def contact(request):
    # cache.set("name", "ashkan", 50)
    # context = {"title": "صفحه اصلی", "name": "ashkan",
    #            "age": 19, "role": "customer"}
    return render(request, 'contact.html')  # , context)


@csrf_exempt
@permission_classes((permissions.AllowAny,))
def galery(request):
    # cache.set("name", "ashkan", 50)
    # context = {"title": "صفحه اصلی", "name": "ashkan",
    #            "age": 19, "role": "customer"}
    return render(request, 'galery.html')  # , context)
