from polls.models import Poll, PollTranslation, Language
from polls.models import Choice
from django.contrib import admin

class PollTranslationInline(admin.TabularInline):
    model = PollTranslation
    extra = 1
    
    def get_formset(self, request, obj=None, **kwargs):
        self.max_num = Language.objects.all().count();
        return super(PollTranslationInline, self).get_formset(request, obj, **kwargs);
    
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        #kwargs['queryset'] = Language.objects.all();
        kwargs['initial'] = Language.objects.get(pk=3);
        formfield = super(PollTranslationInline, self).formfield_for_foreignkey(db_field, request, **kwargs)
        return formfield;

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'was_published_today')
    fieldsets = [
        #(None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline,PollTranslationInline]
    
admin.site.register(Poll, PollAdmin)
