# -*- encoding: UTF-8 -*-

from .models import Project, Agreement
from .sigidi import SigidiConnection
from django.contrib import admin
from django.contrib.admin import helpers
from django.utils.translation import ugettext_lazy as _


@admin.register(Project, Agreement)
class AccountingAdmin(admin.ModelAdmin):

    list_display = ('code', 'gender_equality', 'free_software',)

    list_filter = ('gender_equality', 'free_software',)

    search_fields = ('code', )

    readonly_fields = ('code',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        """ Remove action delete object from list of actions """
        actions = super(AccountingAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def reload(self, request, queryset):
        try:
            sigidi = SigidiConnection()
            sigidi.update_entities(Project, Agreement)
            self.message_user(
                request, _(u'Se ha actualizado el listado con éxito'))
        except:
            self.message_user(
                request, _(u'SIGIDI - Servicio no disponible'), 'error')
    reload.short_description = 'Actualizar listado desde SIGIDI'

    def changelist_view(self, request, extra_context=None):
        if 'action' in request.POST and request.POST['action'] == 'reload':
            if not request.POST.getlist(helpers.ACTION_CHECKBOX_NAME):
                post = request.POST.copy()
                post.update({helpers.ACTION_CHECKBOX_NAME: None})
                request._set_post(post)
        return super(AccountingAdmin, self).changelist_view(
            request, extra_context)

    actions = ('reload', )