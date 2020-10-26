from django.db import models
# from datetime import datetime

class SettingsModel(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    
    frequencyfollow = models.IntegerField()
    frequencyunfollow = models.IntegerField()
    frequencypostcheck = models.IntegerField( null=True, blank=True)
    daysafterunfollow = models.IntegerField()
    
    state = models.BooleanField(default = False)

    suspicion = models.BooleanField(default = False)

    suspicioncode = models.CharField(max_length=100, null=True, blank=True)

    emailsuspicion = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"
        