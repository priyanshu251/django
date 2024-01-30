from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# creating router object
router = DefaultRouter()

#register StudentModelViewSet in router 
router.register('studentapi', views.StudentModelViewSet,basename='student')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include(router.urls)),
    path("auth/",include("rest_framework.urls",namespace="rest_framework")),
]

# http http://127.0.0.1:8000/studentapi/ 'Authorization:Token a91b566c1c985ebd3ef6aa5ee8409bec89fc5d1d' 
# http POST http://127.0.0.1:8000/studentapi/ name=akshaj roll=7 city=kalyani 'Authorization:Token      a91b566c1c985ebd3ef6aa5ee8409bec89fc5d1d'
# http PUT http://127.0.0.1:8000/studentapi/3/ name=akshaj roll=9 city=kalyani 'Authorization:Token a91b566c1c985ebd3ef6aa5ee8409bec89fc5d1d'