from django.conf import settings
from django.core.mail import send_mail

def send_email(email,token):
    try:
        subject = 'Verify your acccount'
        message = f'Hey dear, please click the link to verify your account in our website. http://127.0.0.1:8000/verify/{str(token)}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

    except Exception as e:
        return Response(e)