from django import forms
from django.contrib import admin
from multilingual.flatpages.models import MultilingualFlatPage
from django.utils.translation import ugettext_lazy as _
from multilingual.admin import MultilingualModelAdmin, MultilingualModelAdminForm
#wd
from ckeditor.widgets import CKEditorWidget

class MultilingualFlatpageForm(MultilingualModelAdminForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes."),
        error_message = _("This value must contain only letters, numbers,"
                          " underscores, dashes or slashes."))

    class Meta:
        model = MultilingualFlatPage


class MultilingualFlatPageAdmin(MultilingualModelAdmin):
    form = MultilingualFlatpageForm
    use_fieldsets = (
        (None, {'fields': ('title', 'url', 'sites', 'content')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

    #wd fix
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(MultilingualFlatPageAdmin,self).formfield_for_dbfield(db_field,**kwargs)
        if db_field.name == 'content':
            formfield.widget = CKEditorWidget(config_name='full_ckeditor')
            return formfield
        return formfield  

admin.site.register(MultilingualFlatPage, MultilingualFlatPageAdmin)
