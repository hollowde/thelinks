from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Region

class RegionSerializer(GeoFeatureModelSerializer):
    model = Region