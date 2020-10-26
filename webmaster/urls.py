# from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'webmaster'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='Login'),
    path('index/', IndexView.as_view(), name='Index'),
    path('codesubmit/', CodeView.as_view(), name='Code-Submit'),
]
