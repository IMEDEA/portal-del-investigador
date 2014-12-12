# -*- encoding: UTF-8 -*-

from cvn import settings as st_cvn
from cvn.models import CVN
from django.conf import settings as st
from django.core.files.move import file_move_safe
from django.core.management.base import BaseCommand
from cvn.helpers import get_cvn_path

import os


class Command(BaseCommand):
    help = u'Reorganiza la hubicación de los CVN-PDF'

    def handle(self, *args, **options):
        for cvn in CVN.objects.all():
            try:
                filename = u'CVN-%s.pdf' % cvn.user_profile.documento
                pdf_path = get_cvn_path(cvn, filename)
                new_pdf_path = os.path.join(st.MEDIA_ROOT, pdf_path)

                filename = u'CVN-%s.xml' % cvn.user_profile.documento
                xml_path = get_cvn_path(cvn, filename)
                new_xml_path = os.path.join(st.MEDIA_ROOT, xml_path)

                root_path = '/'.join(new_pdf_path.split('/')[:-1])
                if not os.path.isdir(root_path):
                    os.makedirs(root_path)

                if cvn.cvn_file.path != new_pdf_path:
                    file_move_safe(
                        cvn.cvn_file.path, new_pdf_path, allow_overwrite=True)
                    cvn.cvn_file.name = pdf_path

                if cvn.xml_file.path != new_xml_path:
                    file_move_safe(
                        cvn.xml_file.path, new_xml_path, allow_overwrite=True)
                    cvn.xml_file.name = xml_path

                cvn.save()
            except Exception as e:
                print 'User: %s - CVN: %s' % (
                    cvn.user_profile.user, cvn.cvn_file)
                print '%s (%s)' % (e.message, type(e))
