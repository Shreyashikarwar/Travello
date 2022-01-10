from django.shortcuts import render
from django.views import generic
from .models import services
from home.models import section
# Create your views here.

class ServicesView(generic.View):
    def get(self, request, *args, **kwargs):
        data = services.objects.all()[0:1]
        title = section.objects.all()

        return render (request, 'services/services.html', {'data':data, 'title':title})