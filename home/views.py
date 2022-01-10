from django.shortcuts import render
from django.views import generic
from .models import booking, testimony, section, intro
from django.db.models import Q
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from news.models import news, discount
# Create your views here.

class HomeView(generic.View):
    def get(self, request, *args, **krargs):
        count = booking.objects.filter(offer=True).count()
        counttest = testimony.objects.count()
        newscount = news.objects.count()
        newsdata = news.objects.all()
        title = section.objects.all()
        citydata = booking.objects.all()
        testdata = testimony.objects.all()
        introdata = intro.objects.all()
        newsdisc = discount.objects.all()
        return render(request, 'home/index.html', {'newsdata':newsdata, 'citydata':citydata, 'testdata':testdata,
         'title':title, 'introdata': introdata, 'newsdisc': newsdisc, 'count':count, 'counttest':counttest, 'newscount':newscount  })


class SearchView(generic.View):
    def get(self, request, *args, **krargs):
        if 'search' in request.GET:
            search = request.GET['search']
            print(search)
            cdata = booking.objects.filter(Q(city__icontains=search)).distinct()
            print(cdata)
            count = booking.objects.filter(offer=True).count()
            counttest = testimony.objects.count()
            newscount = news.objects.count()
            title = section.objects.all()
            citydata = booking.objects.all()
            newsdisc = discount.objects.all()
            testdata = testimony.objects.all()
            introdata = intro.objects.all()
            newsdata = news.objects.all()
            return render(request, 'home/index.html', {'cdata':cdata, 'newsdata':newsdata, 'citydata':citydata, 'testdata':testdata,
         'title':title, 'introdata': introdata, 'newsdisc': newsdisc, 'count':count, 'counttest':counttest, 'newscount':newscount } )
            # return HttpResponseRedirect(reverse('homeview') ,{'cdata':cdata})
        # else:
        #     cdata = booking.objects.all()
        #     return render(request, 'home/search.html', {'cdata':cdata})
