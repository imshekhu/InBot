from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webmaster.urls', namespace="webmaster"))
    #  path('site/', include('datagathering.urls', namespace ="data")),
]
