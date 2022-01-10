from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.expressions import F
from django.db.models.fields import BLANK_CHOICE_DASH
# Create your models here.

class section(models.Model):
    bgimghead = models.ImageField(blank=True, null=True)
    bgimgfoot = models.ImageField(blank=True, null=True)
    bgtit = RichTextField(blank=True, null=True)
    secsub = RichTextField(null=True, blank=True)
    sectitle = RichTextField(null=True, blank=True)

    def __str__(self):
        return "Title is " + self.sectitle

class intro(models.Model):
    introtitle = RichTextField(null=True, blank=True)
    introdesc = RichTextField(null=True, blank=True)
    introimg = models.FileField(null=True, blank=True)

class booking(models.Model):
    city = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    desc = RichTextField(null=True, blank=True)
    offer = models.BooleanField(default=False)
    price= RichTextField(null=True, blank=True)

    def __str__(self):
        return "Travel to " + self.city

class testimony(models.Model):
    desc = RichTextField(null=True, blank=True)
    client = RichTextField(null=True, blank=True)