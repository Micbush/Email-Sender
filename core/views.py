from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
import re
from django.template.loader import render_to_string, get_template

# from . import emails


def index(request):
    if request.method =="POST":
        data=request.POST
        subject=data['subject']
        message=data['content']
        email_to=data['email']
        email_list = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", email_to)
        
        # subject = 'Music Downloading Site'
        # message ='For intresting and any genre of music of your liking kindly visit our website and browse through for free at larsonbro.com'
        email_from =settings.EMAIL_HOST_USER
        ctx = {

            'content': message

        }

        message = get_template('mail.html').render(ctx)
        

        print(email_list)
        send_mail(subject, message, email_from, email_list)
        # print('Sent Successfully')
    return render(request, 'index.html')


































# lqvejyjuqlcnmshx