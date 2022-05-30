from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Toestco.views import redis_test, hello_world, index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    # path('', include, name='index'),
    # path('ss/', redis_test.as_view()),
    # path('sss/', hello_world),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('API/', include('Toestco.urls')),
    path('auth/', include('user_login_register.urls')),


]





# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ3MjQ0MzU0LCJpYXQiOjE2NDcyNDQwNTQsImp0aSI6ImM1ZDc0M2Q1OGUwMzQxMDM4ZDJjNWQ2ODYzNjkxNzdiIiwidXNlcl9pZCI6MX0.Qb31loPG9_ggcc-AR4f4TT84nfhMzCsX2pTznXGDH04