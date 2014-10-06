# -*- encoding: UTF-8 -*-

from django.conf import settings as st
from django.core.mail import EmailMessage
from smtplib import SMTPRecipientsRefused
import logging

logger = logging.getLogger('default')


def send_mail(subject, body, email_to):
    if st.EMAIL_DEBUG:
        email_to = st.EMAIL_DEBUG_ADDRESS
    msg = EmailMessage(subject, body, to=[email_to])
    msg.content_subtype = "html"
    try:
        msg.send()
    except SMTPRecipientsRefused as e:
        logger.error('Error en el envío: ' + str(e))
