from products.models.product import Product
from products.models.productimage import ProductImage
from django.contrib import admin
from widgets.adminimagewidget import AdminImageWidget
from django.db import models
from sorl.thumbnail.admin import AdminImageMixin, AdminClearableImageWidget
from ckeditor.widgets import CKEditorWidget
from multilingual.admin import MultilingualModelAdmin, MultilingualModelAdminForm
from django.db.models.fields import CharField
from django import forms
from products.models.productsize import ProductSize
from products.models.device import Device
from django.contrib.admin.options import ModelAdmin


class ImageInline(AdminImageMixin, admin.TabularInline):
    #formfield_overrides = {
    #    models.ImageField: {'widget': AdminImageWidget},
    #}    
    model = ProductImage
    readonly_fields = ( 'image_width', 'image_height' )
    extra = 1

class SizeInline(admin.TabularInline):
    model = ProductSize
    fields = ( 'width', 'height' )
    extra = 1

class ProductForm(MultilingualModelAdminForm):
    #description = forms.CharField(widget=CKEditorWidget)
    model = Product

class DeviceAdmin(ModelAdmin):
    model = Device

class ProductAdmin(MultilingualModelAdmin):
    form = ProductForm
    list_display = ('name', 'visible')
    
    use_fieldsets = [
        ('General', {'fields': ['visible','name','material','description','stock',] }),
        #('Size', {'fields' : [ 'width', 'height'] }),
        ('Price', { 'fields' : ['price'] } ),
        ('Related products', {'fields': ['related'] }),
        ('Related devices', {'fields': ['devices'] }),

        #('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    
    inlines = [SizeInline, ImageInline]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ProductAdmin,self).formfield_for_dbfield(db_field,**kwargs)
        if db_field.name == 'description':
            formfield.widget = CKEditorWidget()
            return formfield
        return formfield    

admin.site.register(Product, ProductAdmin)
admin.site.register(Device, DeviceAdmin)
