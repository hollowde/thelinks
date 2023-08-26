from wagtail import hooks
from .views import region_viewset, region_chooser_viewset


@hooks.register("register_admin_viewset")
def register_viewset():
    return region_viewset


@hooks.register("register_admin_viewset")
def register_viewset():
    return region_chooser_viewset
