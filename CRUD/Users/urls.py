from django.urls import path
from . views import Userdata
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("Usercreation", Userdata.as_view(), name="Userdata"),
    path("login", jwt_views.TokenObtainPairView.as_view(), name="login"),
]
