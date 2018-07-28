import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
import os
from sorl.thumbnail import ImageField


class ImageModel(models.Model):
    #image = models.ImageField(upload_to ="products/")
    image = ImageField(upload_to ="products/",blank=True)
    default = models.BooleanField();
    image_height = models.IntegerField()
    image_width = models.IntegerField()
    
    class Meta:
        abstract = True
    
#    def __str__(self):
#        return "%s"%self.title
    
    def __unicode__(self):
        return self.image.__str__();
        
    def save(self, force_update=False, force_insert=False, thumb_size=(180,300)):

        image = Image.open(self.image)
        
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
            
        # save the original size
        self.image_width, self.image_height = image.size
        """
        image.thumbnail(thumb_size, Image.ANTIALIAS)
        
        # save the thumbnail to memory
        temp_handle = StringIO()
        image.save(temp_handle, 'png')
        temp_handle.seek(0) # rewind the file
        
        # save to the thumbnail field
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1],
                                 temp_handle.read(),
                                 content_type='image/png')
        self.thumbnail.save(suf.name+'.png', suf, save=False)
        self.thumbnail_width, self.thumbnail_height = image.size
        """
        # save the image object
        super(ImageModel, self).save(force_update, force_insert)