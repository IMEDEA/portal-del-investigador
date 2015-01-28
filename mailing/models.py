# -*- encoding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from mailing import settings as st_mail


class Email(models.Model):
    entry_type = models.IntegerField(
        _(u'Tipo'), choices=st_mail.MAIL_TYPE, null=False, unique=True)

    title = models.CharField(_(u'Título'), max_length=255, blank=False)

    content = models.TextField(_(u'Contenido'), blank=False)

    is_active = models.BooleanField(_(u'Activo'), default=False)

    def __unicode__(self):
        return st_mail.MailType(self.entry_type).name