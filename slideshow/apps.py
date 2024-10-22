from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SlideshowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'slideshow'
    verbose_name = _("Slide Show")
