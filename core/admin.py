# -*- encoding: UTF-8 -*-


from core import settings as stCore
from core.models import UserProfile, Log
from django import forms
from django.conf import settings as st
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage, Site
from django.forms.widgets import HiddenInput, MultipleHiddenInput
from tinymce.widgets import TinyMCE

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0

UserAdmin.list_display = (
    'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff'
)

UserAdmin.inlines = [
    UserProfileInline,
]


class LogAdmin(admin.ModelAdmin):
    list_display = ('application', 'entry_type', 'user_profile', 'date')
    list_filter = ('entry_type', 'application')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_actions(self, request):
        """ Remove action delete object from list of actions """
        actions = super(LogAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def get_readonly_fields(self, request, obj=None):
        return tuple(Log._meta.get_all_field_names())


class PageForm(FlatpageForm):

    url = forms.CharField(label='', max_length=100, required=False)
    sites = forms.ModelMultipleChoiceField(queryset=Site.objects.all(),
                                           required=False, label='')

    def __init__(self, *args, **kwargs):
        super(FlatpageForm, self).__init__(*args, **kwargs)
        self.fields['url'].initial = stCore.BASE_URL_FLATPAGES
        self.fields['url'].widget = HiddenInput()
        self.fields['sites'].widget = MultipleHiddenInput()

    def clean_sites(self):
        return [Site.objects.get(id=st.SITE_ID)]

    def save(self, commit=True):
        flatpage = super(PageForm, self).save(commit=False)
        flatpage.save()
        flatpage.url = stCore.BASE_URL_FLATPAGES + str(flatpage.id) + '/'
        return flatpage

    class Meta:
        model = FlatPage
        widgets = {
            'content': TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }


class PageAdmin(FlatPageAdmin):
    form = PageForm
#    fieldsets = (
#        (None, {'fields': ('title', 'content')}),
#    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Log, LogAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
