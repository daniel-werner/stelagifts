from django.contrib.admin.widgets import AdminFileWidget
#from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.conf import settings
import Image
from sorl.thumbnail import get_thumbnail
#import os
#from sorl.thumbnail.main import DjangoThumbnail


def thumbnail(image_path):
    #t = DjangoThumbnail(relative_source=image_path, requested_size=(80, 80))
    im = get_thumbnail(image_path, '100x100', crop='center', quality=99)
    return u'<img src="%s" alt="%s">' % (im.url, image_path)


class AdminImageWidget(AdminFileWidget):
    """
    A FileField Widget that displays an image instead of a file path
    if the current file is an image.
    """
    def render(self, name, value, attrs=None):
        output = []
        if value:
            file_path = '%s%s' % (settings.MEDIA_URL, value)
            try:
                output.append('<a target="_blank" href="%s">%s</a><br />' %
                        (file_path, thumbnail(value)))
            except IOError:
                output.append('%s <a target="_blank" href="%s">%s</a> <br />%s ' %
                        ('Currently:', file_path, value, 'Change:'))

        output.append(super(AdminImageWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))