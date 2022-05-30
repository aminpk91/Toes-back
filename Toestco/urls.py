from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import SubjectViewSet, PhotoViewSet, Post_ViewSet, Sidebar_ViewSet, Product_ViewSet, aboute, contact, galery

router = routers.DefaultRouter()
router.register('Tilte', SubjectViewSet)
router.register('photo', PhotoViewSet)
router.register('active_post', Post_ViewSet, basename='active_post')
router.register('active_sidebar', Sidebar_ViewSet, basename='active_sidebar')
router.register('product', Product_ViewSet, basename='Product')

urlpatterns = [
    path('', include(router.urls)),
    path('aboute', aboute, name='aboute'),
    path('contact', contact, name="contact"),
    path('galery', galery, name="galery"),

]
