from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class aboutus(models.Model):
    bgimg = models.ImageField(blank=True, null=True)
    title = RichTextField(blank=True, null=True)
    details1 = RichTextField(blank=True, null=True)
    details2 = RichTextField(blank=True, null=True)
    # details1 = models.TextField(max_length=300)
    # details2 = models.TextField(max_length=500)
    image = models.ImageField()

class chooseustitle(models.Model):
    title = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

class chooseus(models.Model):
    titler1 = RichTextField(blank=True, null=True)
    reason1 = RichTextField(blank=True, null=True)
    image1 = models.ImageField(blank=True, null=True)

class team(models.Model):
    title = RichTextField(blank=True, null=True)
    titler1 = RichTextField(blank=True, null=True)
    reason1 = RichTextField(blank=True, null=True)
    image1 = models.ImageField(blank=True, null=True)
    titler2 = RichTextField(blank=True, null=True)
    reason2 = RichTextField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    titler3 = RichTextField(blank=True, null=True)
    reason3 = RichTextField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)