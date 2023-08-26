from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


# Class modeling the different regions of The Links, Incorporated
class Region(models.Model):
    REGIONS = (
        ("Eastern Area", "Eastern Area"),
        ("Southern Area", "Southern Area"),
        ("Central Area", "Central Area"),
        ("Western Area", "Western Area"),
    )
    name = models.CharField(
        _("Regional Chapter Name"), max_length=150, choices=REGIONS, unique=True
    )
    description = models.TextField(_("Region Description"))
    mpoly = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name



