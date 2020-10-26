from django.db import models
# from datetime import datetime

class TargetModel(models.Model):
    
    link = models.CharField(max_length=100, null=True, blank=True)
    
    is_followed_ever = models.BooleanField(default=False)
    is_unfollowed = models.BooleanField(default=False)
    
    followed_at = models.DateTimeField(null=True, blank=True)

    unfollowed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.link