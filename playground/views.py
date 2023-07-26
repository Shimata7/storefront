from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
    
    #send_mail('subject', 'message', 'sendermail', ['list o mails reciever'])
    #try:
        #send_mail('subject', 'message', 'mlopez@ec.krugercorp.com', ['lopezsmauricio@gmail.com'])
        #mail_admins('subject','message', html_message='message')
        #message = EmailMessage('Subject', 'Message','from@mau.com', ['lopezsmauricio@gmail.com'])
        #message.attach_file('playground/static/images/wine.jpg')
        #message.send()
        #message = BaseEmailMessage(
            #template_name='emails/hello.html',
            #context={'name': 'Mau'}
        #)
        #message.send(['lopezsmauricio@gmail.com'])
    #except BadHeaderError:
        #pass

    notify_customers.delay('Hello')

    return render(request, 'hello.html', {'name': 'Mosh'})
 