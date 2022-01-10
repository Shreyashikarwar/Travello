from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class news(models.Model):
    date = RichTextField(null=True, blank=True)
    month = RichTextField(null=True, blank=True)
    heading = RichTextField(null=True, blank=True)
    subhead = RichTextField(null=True, blank=True)
    desc = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    bgimg = models.ImageField(null=True, blank=True)

    def __str__(self):
        return 'News "' + self.heading +'"'

class discount(models.Model):
    discountimg = models.ImageField(null=True, blank=True)
    discount = RichTextField(null=True, blank=True)
    discountsub = RichTextField(null=True, blank=True)
