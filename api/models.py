from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    text = models.CharField(max_length=120)
    def __str__(self):
        return self.name








        
