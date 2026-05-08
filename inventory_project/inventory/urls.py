from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('web-login/', views.WebLoginView.as_view(), name='web_login'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('api/home/', views.HomePageAPI.as_view(), name='home_api'),
]