from wagtail.admin.viewsets.model import ModelViewSet
from wagtail.admin.viewsets.chooser import ChooserViewSet
from .models import Region


class RegionViewSet(ModelViewSet):
    model = Region
    form_fields = ["name", "description", "mpoly"]
    icon = "list-ul"


region_viewset = RegionViewSet("region")  # defines /admin/region/ as a base url


class RegionChooserViewSet(ChooserViewSet):
    # The model can be specified as either the model class or an "app_label.model_name" string;
    # using a string avoids circular imports when accessing the StreamField block class (see below)
    model = "_region.Region"

    icon = "list-ul"
    choose_one_text = "Select a region"
    choose_another_text = "Select another region"
    edit_item_text = "Edit this region"
    form_fields = ["name"]  # fields to show in the "Create" tab


region_chooser_viewset = RegionChooserViewSet("person_chooser")
