from email.mime import text
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name, receiver):
    subject = 'Welcome to Ian Awwards clone'
    sender= 'ian.wanjira@student.moringaschool.com'

    html_content = render_to_string('email/awardemail.html', {'name':name})
    text_content = render_to_string('email/awardemail.txt', {'name':name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text_content')
    # msg.send()