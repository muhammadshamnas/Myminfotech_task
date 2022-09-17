from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views
from . views import StoreDataCreation,StoreListView,TodoDetail,StoreList

urlpatterns = [
    path("login", jwt_views.TokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("StoreDataCreation", StoreDataCreation.as_view(), name="StoreDataCreation"),
    path("StoreListView", StoreListView.as_view(), name="StoreListView"),
    path('todos/<int:pk>', TodoDetail.as_view(),name="StoreListView"),
    path('StoreList', StoreList.as_view()),
    
    
]