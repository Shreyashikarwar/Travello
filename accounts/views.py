from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.views import generic
from home.models import section
from django.urls import reverse




# Create your views here.

class SignupView(generic.View):
    def get(self, request, *args, **kwargs):
        title = section.objects.all()
        return render(request, 'accounts/signup.html', {'title': title})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        print(username)
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return render(request, 'accounts/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return render(request, 'accounts/signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                print(user)
                user.save()
                messages.success(request, 'User signned in.')
                return HttpResponseRedirect(reverse('homeview'))        
        else:
            messages.info(request, 'Password does not match')
        return render(request, 'accounts/signup.html')

class SigninView(generic.View):
    def get(self, request, *args, **kwargs):
        title = section.objects.all()
        return render(request, 'accounts/signin.html', {'title': title})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User Logged In')
            return HttpResponseRedirect(reverse('homeview'))

        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'accounts/signin.html')
            

def LogoutView( request, *args, **kwargs):
    if request.method == 'GET':
        print('yup')
        auth.logout(request)
        print('hi')
        messages.success(request, 'User Logged Out')
        return HttpResponseRedirect(reverse('homeview')) 
# class LogoutView(generic.View):
#     def get ( request, *args, **kwargs):
#         print('yup')
#         auth.logout(request)
#         print('hi')
#         messages.success(request, 'User Logged Out')
#         return render(request, 'home/index.html')

