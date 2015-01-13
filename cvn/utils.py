# -*- encoding: UTF-8 -*-

from django.core.exceptions import ObjectDoesNotExist
from lxml import etree
from cvn.parsers.read_helpers import parse_nif
from cvn import settings as st_cvn
from django.utils.translation import ugettext as _


def cvn_to_context(user, context):
    try:
        context['cvn'] = user.cvn
        context['cvn_status'] = st_cvn.CVN_STATUS[user.cvn.status][1]
        if user.cvn.status == st_cvn.CVNStatus.INVALID_IDENTITY:
            if user.cvn.xml_file.closed:
                user.cvn.xml_file.open()
            xml_tree = etree.parse(user.cvn.xml_file)
            user.cvn.xml_file.seek(0)
            nif = parse_nif(xml_tree)
            user.cvn.xml_file.close()
            if nif is not '':
                context['nif_invalid'] = nif.upper()
    except ObjectDoesNotExist:
        return


def scientific_production_to_context(user_profile, context):
    try:
        if not user_profile.cvn.is_inserted:
            return False
        context['Articulos'] = user_profile.articulo_set.all()
        context['Capitulos'] = user_profile.capitulo_set.all()
        context['Libros'] = user_profile.libro_set.all()
        context['Congresos'] = user_profile.congreso_set.all()
        context['Proyectos'] = user_profile.proyecto_set.all()
        context['Convenios'] = user_profile.convenio_set.all()
        context['TesisDoctorales'] = user_profile.tesisdoctoral_set.all()
        context['Patentes'] = user_profile.patente_set.all()
        return True
    except ObjectDoesNotExist:
        return False


def stats_to_context(request, context):
    """Fills context with info from stats"""
    dept, dept_json = None, None
    area, area_json = None, None
    try:
        from statistics.models import Department, Area
        from statistics import settings as st_stat
    except:
        pass
    else:
        context['validPercentCVN'] = st_stat.PERCENTAGE_VALID_CVN
        if 'dept' in request.session and 'dept_json' in request.session:
            dept = Department.objects.get(name=request.session['dept'])
            dept_json = request.session['dept_json']
            context['department'] = dept
            context['label_dept'] = _(u'Departamento')
        if 'area' in request.session and 'area_json' in request.session:
            area = Area.objects.get(name=request.session['area'])
            area_json = request.session['area_json']
            context['area'] = area
            context['label_area'] = _(u'Área')
    return dept, dept_json, area, area_json


def isdigit(obj):
    if type(obj) is str and obj.isdigit():
        return True
    else:
        return False
