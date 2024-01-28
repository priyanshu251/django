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
    path("gettoken/",obtain_auth_token) # ye as function view hai isliye bas aise hi likh diye agar ye class view hota to "obtain_auth_token.asView()" likhte
    #gettoken ki jagah naam kuch bhi likh skte hai, iss url pe hit hone pe obtain_auth_token function hit hoga joki authtoken k view me hai 
    
]

