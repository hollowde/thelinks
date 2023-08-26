from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from _region.models import Region
from _state.models import State, Country


# Local Chapters Associated with regional chapters
class Chapter(models.Model):
    name = models.CharField(_("Chapter Name"), max_length=200, blank=False)
    parent = models.ForeignKey(Region, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(_("Street Address"), blank=False)
    city = models.CharField(_("Chapter City"), blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=False)
    zip = models.CharField(_("Parent Chapter"))
    location = models.PointField(_("Chapter Location"), srid=4326)

    def __str__(self):
        return self.name.split[0]
