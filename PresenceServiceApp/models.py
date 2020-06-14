from django.db import models
from django.conf import settings 

class Profile(models.Model):
    user = models.CharField(max_length=50, default="" , primary_key=True)
    status = models.BooleanField(default=False)
    pic = models.ImageField(upload_to='profile')

    def __str__(self):
        return self.user