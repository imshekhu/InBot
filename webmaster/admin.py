from django.contrib import admin

# Register your models here.

from webmaster.models import SettingsModel, TargetModel

admin.site.register(SettingsModel)
admin.site.register(TargetModel)