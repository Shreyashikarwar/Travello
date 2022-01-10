from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import generic
from .models import contact, contactus
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from home.models import section
# Create your views here.

class ContactView(generic.View):
    def get(self, request, *args, **kwargs):
        title = section.objects.all()
        cont = contact.objects.all()

        return render(request, 'contact/contact.html', {'title':title, 'cont':cont})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['msg']
        send_mail(
            subject, #subject
            msg , #message
            email, #email
            ['tdigimonk@gmail.com', 'shreyash.sikarwar2012@gmail.com'], #to email
        )

        contactdata = contactus(username=username, email=email, subject=subject, msg=msg)
        print(contactdata)
        contactdata.save()
        return HttpResponseRedirect(reverse('contactview'))
        # EMAIL send
        # data_content = {"username": username, "email": email, "subject": subject, "msg": msg,
        #                     "BASE_URL": settings.BASE_URL}
        #email_content = render_to_string('email_templates/email_send_for_contact_us.html', data_content)
        # m = email
        # m['Subject'] = str(username)+ 'Wants to contact you.'
        # m['From'] = email.utils.formataddr((settings.SENDER_NAME, settings.DEFAULT_FROM_EMAIL))
        # m['To'] = settings.EMAIL_HOST_USER
        # m.add_header('Content-Type', 'text/html')
        # m.set_payload(email_content)
        # s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
        # s.ehlo()
        # s.starttls()
        # s.ehlo()
        # s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        # s.sendmail(settings.DEFAULT_FROM_EMAIL, [m['To']], m.as_string())
        # return render(request, 'contact/contact.html')