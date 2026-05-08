from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.views import LoginView as AuthLoginView

class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Customize response if needed
        return response

class WebLoginView(AuthLoginView):
    template_name = 'login.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

# Placeholder API endpoint for homepage data
class HomePageAPI(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Inventory Home Page"})
# Home page placeholders
