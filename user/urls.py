from django.urls import path
from user import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("userprofile",views.UserProfileView,basename="userprofile")

urlpatterns=[
    path("register/",views.SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
]+router.urls