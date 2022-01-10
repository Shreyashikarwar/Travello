from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class services(models.Model):
    why = RichTextField(blank=True, null=True)
    desc =  RichTextField(blank=True, null=True)
    image1 = models.ImageField(null=True, blank=True)
    title1 = RichTextField(blank=True, null=True)
    details1 = RichTextField(blank=True, null=True)
    title2 = RichTextField(blank=True, null=True)
    image2 = models.ImageField(null=True, blank=True)
    details2 = RichTextField(blank=True, null=True)
    title3 = RichTextField(blank=True, null=True)
    image3 = models.ImageField(null=True, blank=True)
    details3 = RichTextField(blank=True, null=True)