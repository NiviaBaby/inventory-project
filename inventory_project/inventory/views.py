from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.contrib.auth.views import LoginView as AuthLoginView

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Customize response if needed
        return response

class WebLoginView(AuthLoginView):
    template_name = 'login.html'
