from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from contact.models import ContactMessage

def make_read(modeladmin, request, queryset):
    queryset.update(read=True)
make_read.short_description = "Mark selected messages as read"


class MessageAdmin(ModelAdmin):
    model = ContactMessage
    
    list_display = ( 'name', 'subject', 'email', 'created', 'status')
    ordering = ['-created']
    actions = [make_read]
    
    def has_add_permission(self, request):
        return False
    
    

admin.site.register(ContactMessage, MessageAdmin)
