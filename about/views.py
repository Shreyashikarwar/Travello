from django.shortcuts import render
from django.views import generic
from home.models import section
from .models import aboutus, chooseus, team, chooseustitle
# Create your views here.

class AboutView(generic.View):

    def get(self, request, *args, **kwargs):

        # about_data = get_object_or_404(AboutUs)
        about_data = aboutus.objects.all()[0:1]
        choosetitle =  chooseustitle.objects.all()[0:1]
        choosedata =  chooseus.objects.all()
        teamdata =  team.objects.all()[0:1]
        title = section.objects.all()
        

        return render(request, 'about/about.html', {'about_data': about_data,
                                                    'choosedata':choosedata,
                                                    'teamdata':teamdata,
                                                    'title':title,
                                                    'choosetitle':choosetitle})
