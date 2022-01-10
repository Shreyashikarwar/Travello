from django.db import models
# Create your models here.

class contact(models.Model):
    bgimg = models.ImageField(null=True, blank=True)

class contactus(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=20, null=True, blank=True)
    msg = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return self.username +" Wants to contact"