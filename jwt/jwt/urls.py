from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# creating router object
router = DefaultRouter()

#register StudentModelViewSet in router 
router.register('studentapi', views.StudentModelViewSet,basename='student')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_oair'), # agar is path pe hit hota hai to ye class "ToenObtainPairView" call hoga joki iss package "simple jwt" me views.py me hai---------iska kaam hai access token aur refresh token provide karna
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'), # ye class refresh token provide karega
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'), # ye class verify karega ki token valid hai ya nahi
]

