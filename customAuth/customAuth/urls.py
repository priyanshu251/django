from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token #restframework me authtoken me views file hai jisme obtain_auth_token ek function hoga uska kaam hai token generate krna 

# creating router object
router = DefaultRouter()

#register StudentModelViewSet in router 
router.register('studentapi', views.StudentModelViewSet,basename='student')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include(router.urls)),
    path("auth/",include("rest_framework.urls",namespace="rest_framework")),
]

