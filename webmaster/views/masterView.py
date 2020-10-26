from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json

from webmaster.services import LoginService, SettingsService


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
   
    def get(self, request):
        template ='login.html'
        return TemplateResponse(request,template)
    
    def post(self, request):
        result = LoginService().loginService(request)
        return result

@method_decorator(login_required, name='dispatch')
class IndexView(View):

    def get(self, request):
        result = SettingsService().settingService(request)
        return result

    def post(self, request):
        result = SettingsService().createOrUpdate(request)
        return result

@method_decorator(csrf_exempt, name='dispatch')
class CodeView(View):
    
    def post(self,request):
        print(request)
        result = SettingsService().submitCode(request)
        return result
