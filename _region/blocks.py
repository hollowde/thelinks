from wagtail import blocks
from .views import region_chooser_viewset

PersonChooserBlock = region_chooser_viewset.get_block_class(
    name="RegionChooserBlock", module_path="_region.blocks"
)

