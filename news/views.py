from django.shortcuts import render
from django.views import generic
from .models import news, discount
from home.models import section
# Create your views here.

class NewsView(generic.View):
    def get(self, request, *args, **kwargs):
        newsdata = news.objects.all()
        title = section.objects.all()
        newsdisc = discount.objects.all()

        return render (request, 'news/news.html', {'newsdata':newsdata, 'title':title, 'newsdisc':newsdisc})